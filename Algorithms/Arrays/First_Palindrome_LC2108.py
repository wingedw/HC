'''
Given an array of strings words, return the first palindromic 
string in the array. If there is no such string, return an 
empty string "".

A string is palindromic if it reads the same forward and 
backward.
'''
def firstPalindrome(words) -> str:
    for x in words:
        if x == x[::-1]:
            return x
    return ""

words = ["abc","car","ada","racecar","cool"]
print(firstPalindrome(words))