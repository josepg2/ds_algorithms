text = "This is the best"

def rev_sentence(text):
    text_ls = text.split()
    text_ls.reverse()

    print(" ".join(text_ls))

rev_sentence(text)