'''
You will receive two lines. The first one will have an encrypted string, which you will have to decode. On the second
line you will receive two letters or substrings, separated by a single space.
First you will have to decode the first line by reducing the ASCII value of each character in it by 3. Then you should
get the two substrings of the second line. You must find every occurrence of the first substring in the now decrypted
text and replace it with the second substring.
Also, you don't know which book you have taken, so you must check if it is valid. A valid text contains only lowercase
letters, from 'd' onwards, and the symbols '{', '}', '|', '#'. If the text is invalid, you should not try to decipher
it and you should print "This is not the book you are looking
'''

text_to_decrypt = input()
cipfer = input()
valid_symbol = ['{', '}', '|', '#']
lord_valid = [chr(i) for i in range(100, 123)]
all_valid_char = valid_symbol + lord_valid

def reduce_char():
    new_text = "".join(chr(i) for i in [ord(i) -3 for i in text_to_decrypt])
    return new_text


if any(i not in all_valid_char for i in text_to_decrypt):
    print(f'This is not the book you are looking for.')
else:
    f_char, s_char = cipfer.split()
    word = reduce_char()
    print(word.replace(f_char, s_char))