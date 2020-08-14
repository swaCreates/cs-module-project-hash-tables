d = {}

def no_dups(s):
    # Your code here

    # loop over string
    # store word in dict
    for list_of_words in s.split():
        duplicate(list_of_words.join(s))
    
    return d

def duplicate(word):
    if word in d:
        return True
    else:
        d[word] = True
        




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))