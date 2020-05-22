text = 'aaaadddddbhdratsrtass'

def str_compression(text):
    
    i = 0
    output = ''

    while i < len(text):
        letter = text[i]
        count = 1
        i += 1 
        while i < len(text) and letter == text[i]:
            count += 1
            i += 1
        output += (letter + str(count))

    print(output)

str_compression(text)