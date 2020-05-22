'''
Needs changes. Not satisfied

'''

text = "   dfasf      ssdAD  "

def rev_sentence(text):
    
    words = []
    start = -1
    output = ''

    for i, letter in enumerate(text) :
        if letter != ' ' and start == -1:
            start = i
        elif letter == ' ' and start != -1:
            words.append(text[start:i])
            start = -1
        elif i == len(text) -1 and start != -1:
            words.append(text[start:])
        
        
    for word in range(len(words)):
        output += (words.pop() + " ")

    print(output[:-1])


rev_sentence(text)