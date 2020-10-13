words = input().split()
searched_palindrome = input()

result = [i for i in words if i == i[::-1]]
print(result)
print(f'Found palindrome {words.count(searched_palindrome)} times')