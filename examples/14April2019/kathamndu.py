'''
Write a program that decrypts messages, which contain information about coordinates. You are looking for names of peaks
in the Himalayas and their geohash coordinates. Keep reading lines until you receive the "Last note" message.
Here is your cipher:
    • Name of the peak
        ◦ It is consisted of letters (upper and lower), numbers and some of the following characters between its
            letters – "!" "@" "#" "$" "?". Example for valid names: “!@K?#2!#” (K2).
    • The length of the geohashcode
        ◦ Begins after the "=" (equals) sign and is consisted only of numbers.
    • The geohash code
        ◦ Begins after these symbols – "<<", may contain anything and the message always ends with it.
Examples for valid input:
"!Ma$$ka!lu!@=9<<ghtucjdhs" – all the components are there – name of the peek, length of the geohashcode and
a geohashcode.
"!@Eve?#rest!#=7<<vbnfhfg"
Examples of invalid input:
"anna@fg<<jhsd@bx!=4" – their order is wrong. The name should be first, the length after and the code last.
"#n...s!n-<<tyuhgf4" – the length is missing and the name contains dots.
'''

import re
pattern = re.compile(r'^([0-9a-zA-Z!@#$?]+)=(\d+)<<(.+)$')


while True:
    letter = input()
    if letter == 'Last note':
        break

    result = pattern.match(letter)
    if result and int(result.group(2)) == len(result.group(3)):
        word = re.sub('[!@#$?]+', '', result.group(1))
        print(f'Coordinates found! {word} -> {result.group(3)}')
    else:
        print(f'Nothing found!')

