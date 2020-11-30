import re

text_string = input()
f_word = []
l_word = []
count = {}

mirror_f = []
mirror_s = []

pattern = re.compile(r'([@|#])(?P<first>[a-zA-Z]{3,})\1\1(?P<second>[a-zA-Z]{3,})\1')

for text in pattern.finditer(text_string):
    f = text.group('first')
    s = text.group('second')
    if f and s:
        f_word.append(f)
        l_word.append(s)

if len(f_word) == 0:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{len(f_word)} word pairs found!")
    for f, s in zip(f_word, l_word):
        if f == s[::-1]:
            mirror_f.append(f)
            mirror_s.append(s)

    if len(mirror_f) == 0:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(", ".join(f'{key} <=> {value}' for key, value in zip(mirror_f, mirror_s)))

"""
On the first line of the input you will be given a text string. In order to win the competition you have to find all hidden word pairs, read them and mark the ones that are mirror images of each other.
First of all you have to extract the hidden word pairs. Hidden word pairs are:
    • Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
    • At least 3 characters long each (without the surrounding symbols)
    • Made up of letters only
If the second word, spelled backwards is the same as the first word and vice versa (casing matters!), then they are a match and you have to store them somewhere. Examples of mirror words: 
#Part##traP# @leveL@@Level@ #sAw##wAs#
    • If you don`t find any valid pairs print: "No word pairs found!"
    • If you find valid pairs print their count: "{valid pairs count} word pairs found!"
    • If there are no mirror words print: "No mirror words!"
    • If there are mirror words print:
"The mirror words are:
{wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, etc…"""

# Input
"""
@mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r	
"""
