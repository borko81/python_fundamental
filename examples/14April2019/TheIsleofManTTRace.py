'''Write a program that decrypts messages. You’re going to receive a few notes that contain the following information:
    • Name of racer
        ◦ Consists only of letters. It is surrounded from the both sides by any of the following symbols – "#, $, %, *,
         &". Both symbols – in the beginning and at the end of the name should match.
    • Length of geohashcode
        ◦ Begins after the "=" sign and it is consisted only of numbers.
    • Encrypted geohash code
        ◦ Begins after these symbols - “!!”. It may contain anything and the message always ends with it.
Examples for valid input:
#SteveHislop#=16!!tv5dekdz8x11ddkc
Examples of invalid input:
%GiacomoAgostini$=7!!tv58ycb – The length is the same, but the name is not surrounded by matching signs.
$GeoffDuke$=6!!tuvz26n35dhe4w4 – The length doesn't match the lengh of the code.
&JoeyDunlop&!!tvndjef67t=14 – The length should be before the code.
The information must be in the given order, otherwise it is considered invalid. The geohash code you are looking for is
with length exactly as much as the given length in the message. To decrypt the code you need to increase the value
of each symbol from the geohashcode with the given length. If you find a match, you have to print the following message:
"Coordinates found! {nameOfRacer} -> {geohashcode}"
and stop the program. Otherwise, after every invalid message print:
"Nothing found!'''

import re

pattern = re.compile(r'^([#,$,%,*,&])(\w+)(\1)=(\d+)!!(.+)$')

while True:
    line = input()
    if line == '':
        break

    result = pattern.search(line)
    if result and int(result.group(4)) == len(result.group(5)):
        word = ''
        increment= int(result.group(4))
        for i in result.group(5):
            word += chr(ord(i) + increment)
        print(f'Coordinates found! {result.group(2)} -> {word}')
        break
    else:
        print('Nothing found!')