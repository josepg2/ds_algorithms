'''
generators are cool
'''

text = "malayalam"

def str_palindromic(text):
    print("palindromic") if all(text[i] == text[~i] for i in range(len(text)//2)) else print("Not palindromic")

str_palindromic(text)