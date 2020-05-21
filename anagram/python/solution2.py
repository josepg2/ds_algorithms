'''
Solution using dictionary
'''

def anagram():
    s1 = "clint eastwood "
    s2 = "old west action"

    count = {}

    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    if len(s1) != len(s2):
        print("The strings are not anagrams")
        return False

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            print("The strings are not anagrams")
            return True

    print("The stings are anagrams")
    return True

anagram()