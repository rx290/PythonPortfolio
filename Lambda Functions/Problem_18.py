"""
Write a Python program to find palindromes in a given list of strings using Lambda.
Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']
""" 
lst = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
palindrome = []
palindrome_finder = lambda x: palindrome.append(x) if x == x[::-1] else print(x, "is not palindrome.")
list(map(palindrome_finder,lst))
print("list of palindromes: ",palindrome)