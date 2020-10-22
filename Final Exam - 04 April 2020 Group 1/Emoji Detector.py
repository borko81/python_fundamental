import re
from functools import reduce

string = input()
countOfAllEmojis = []

pattern = re.compile(r'(:{2}|\*{2})([A-Z]{1}[a-z]{2,})(\1)')
found_digit = re.findall(r'\d+', string)


for result in pattern.findall(string):
    r = result[1]
    countOfAllEmojis.append(r)

coolThresholdSum = reduce(lambda x, y : x * y, [int(x) for i in found_digit for x in list(i.strip())])

print(f'Cool threshold: {coolThresholdSum}')
print(f'{len(countOfAllEmojis)} emojis found in the text. The cool ones are:')


for result in pattern.findall(string):
    r = result[1]
    if sum(ord(i) for i in r) > coolThresholdSum:
        print("".join(result))



'''INFO---
Your task is to write program which extracts emojis from a text and find the threshold based on the input.
You have to get your cool threshold. It is obtained by multiplying all the digits found in the input. 
The cool threshold could be a very big number, so be mindful.
An emoji is valid when:
    • Is surrounded by either :: or ** (exactly 2)
    • Is at least 3 characters long (without the surrounding symbols)
    • Starts with a capital letter
    • Continues with lowercase letters only
Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::
You need to count all valid emojis in the text and calculate their coolness. The coolness of the emoji is determined
by summing all the ASCII values of all letters in the emoji. 
Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
You need to print the result of cool threshold and after that to take all emojis out of the text, count them and print
the only the cool ones on the console. 
Input
    • On the single input you will receive a piece of string. 
Output
    • On the first line of the output print the obtained Cool threshold in format:
    • Cool threshold: {coolThresholdSum}
On the next line print the count of all emojis found in the text in format:
    • {countOfAllEmojis} emojis found in the text. The cool ones are:
    • {cool emoji 1}
    • {cool emoji 2}
    • {…}'''