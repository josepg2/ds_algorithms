'''
Check if given two strings are anagrams
Spaces can be  ignored
'''


s1 = "go  ds"
s2 = "dog"

s1 = s1.replace(" ", '')
s2 = s2.replace(" ", '')

if sorted(s1) == sorted(s2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")