"""
On the first line, you will receive words separated by a single space.
On the second line, you will receive a palindrome.
First, you should print a list containing all the found palindromes in the sequence.
Then, you should print the number of occurrences of the given palindrome in the format:
"Found palindrome {number} times".
"""

txt = input().split()
word = input()
txt = [data for data in txt if data == data[::-1]]
print(txt)
print(f"Found palindrome {txt.count(word)} times")