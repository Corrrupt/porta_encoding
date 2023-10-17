import re  # regex
from string import punctuation  # pythons list of punctuation
from encoding_table import table  # imports the table needed for encoding

escaped_punctuation = re.escape(punctuation)

message_to_encode = input("Enter the message: ")

while True:  # Keep looping until break condition is met (good key)
    encode_key = input("Enter the key: ")
    # Check validity of key (if it DOESN'T contains numbers [\d], space [\s], or punctuation then break out of the loop)
    if (not re.search(r"\d|\s|[" + escaped_punctuation + "]", encode_key)):
        break
    print("Invalid key.. exclude numbers, spaces, or punctuation")


# gets rid of numbers and punctuation from message and sets it to lowercase
message_to_encode = re.sub(r"\d|[" + escaped_punctuation + "]", "", message_to_encode).lower()


# ----ENCODING FUNCTION UNDER HERE-------
encoded_message = ""
i = 0 # Manually keeping track of index so that we can skip over the encoding of spaces

for x in message_to_encode:
    if x != ' ':
        # maps a letter of the key with the message (uses index modulus length of the key so it repeats the letters of key after goes went over them already)
        key_char = encode_key[i % len(encode_key)].lower()

        # This is what position in the alphabet key_char is
        alphabet_pos = ord(key_char) - 96
        row = (alphabet_pos + 1) // 2 if (alphabet_pos % 2 == 1) else alphabet_pos // 2
        '''
        the "row" variable tells us what index we actually use on the encoding_table
        (this relates to what row we use in the actual table shown in the document)

        ("//" means a floor division.. rounds the result down to the nearest whole number)

        Ex:
        if alphabet_pos is 1 (which is "a") it gets set to 1
        if alphabet_pos is 2 (which is "b") it gets set to 1
        if alphabet_pos is 3 (which is "c") it gets set to 2
        if alphabet_pos is 4 (which is "d") it gets set to 2
        etc..
        '''

        col = ord(x) - 96  # This says what column in the row we need to get
        encoded_letter = table[row-1][col-1] # This pieces it all together.. -1 because python index starts at 0
        encoded_message = encoded_message + encoded_letter

        i += 1
    else:
        encoded_message = encoded_message + " "

print("Encrypted message is", encoded_message)
