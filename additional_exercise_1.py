import random
#1 Open the txt file
with open("number.txt", "r", encoding="utf-8") as f:
    content = f.read()
    #3,4 lowercase and split into tokens
    lower_case_content = content.lower().split()
    #5 Dictionary
    dictionary = {}
    #'b' is a len of tokens, i.e. max value. 'a' is a value that we will add each cycle that represents a key. 'c' is value on 1 bigger than 'a' that represents value (1 next word for every occurrence)
    b = len(lower_case_content)
    a = 0
    while a<b:    
        c = a+1
        if c==b:
            break
        keys = lower_case_content[a]
        value = lower_case_content[c]
        a+=1
        dictionary[keys] = value
    print(dictionary)
    #6 generate text    
    print("Каламбурний текст: ", end=' ')
    for i in range(1,200):
        choice = random.choice(list(dictionary.keys()))
        print(choice, end=' ')
    dictionary  