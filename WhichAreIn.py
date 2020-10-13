'''
Given two lists of strings print a new list of the strings that contains words from the first
list which are substrings
of any of the strings in the second list (only unique values)
'''

f_list = input().split()
s_list = input().split()

result = {i for x in s_list for i in f_list if i in x}

print(list(result))


'''
arp, live, strong
lively, alive, harp, sharp, armstrong
tarp mice bull
lively alive harp sharp armstrong
'''