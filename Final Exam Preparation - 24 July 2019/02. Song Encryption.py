import re

common_one = re.compile(r'(^[A-Z]([a-z,\'\s])+$)')
common_two = re.compile(r'([A-Z, \s])+')
small_range = list(range(97, 123))
big_range = list(range(65, 91))


def check_length(length, symbol):
    increase = ord(symbol)
    total = increase + length

    if total > 90 and symbol.isupper():
        temp = total - 90
        total = big_range[temp - 1]

    if total > 122 and symbol.islower():
        temp = total - 122
        total = small_range[temp - 1]

    return chr(total)


while True:
    line = input()
    if line == 'end':
        break

    artist, song = line.split(":")
    if common_one.match(artist) and common_two.match(song):
        length = len(artist)

        artist = "".join([check_length(length, i) if i not in [" ", "'"] else i for i in artist ])
        song = "".join([check_length(length, i) if i not in [" ", "'"] else i for i in song ])
        print(f"Successful encryption: {artist}@{song}")
    else:
        print("Invalid input!")

# print(ord('V'), ord('V') + 12)
# print(check_length(12, 'V'))


'''
Until you receive the command "end" you should read lines in following format :"{artist}:{song}", and check if it's
 valid, considering the following rules:
    • Artist – starts with capital letter, followed by lowercase letters.
        ◦  It can also contains apostrophe ( ' ), and whitespace " "; 
Valid group name: Red hot chili peppers, Eminem, 	
Invalid group name: ReD Hot CiLly PePers, sLipKnot, guns n'roses
    • Song – contains only capital letters, and whitespaces.
Valid songs: BACK IN BLACK, BLEED IT OUT, KILLSHOT
Invalid songs: #BaCk IN black, BLEED $IT$ OUTt, &KILLSHoT
After you validate the lines of an input, you should encrypt the information. In order to do that, you have to follow 
the rules below:
    • First you need to find a key for encryption.
        ◦ Your key is the length of the artist (e.g. "Eminem" –  key: 6)
    • You have to increment the ASCII value of each symbol of the input, with the key length
(e.g. "char" 'a' -> 'g')
        ◦ Be careful if your key length is bigger than the ASCII value of a letter 'z' or 'Z'. In this case you should
         start from a letter 'a'. (e.g. key:6 letter – 'x', encrypted letter – 'd')
    • You should NOT ENCRYPT the following characters: whitespaces, and apostrophes
    • You also should replace ':' with the sign '@'''