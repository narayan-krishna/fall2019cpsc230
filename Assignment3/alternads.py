#Krishna Narayan
#2327205
#narayan@chapman.edu
#CPSC 230 section 08
#Assignment 3

import string

#clean cleans any inputted string of any white space, numbers, or punctuation
def clean(input_string):
    bad_chars = string.punctuation + string.whitespace + string.digits
    word = input_string
    #running through every character that we do not want:
    for x in bad_chars:
        #replace the characters we do not want with nothing, effectively
        #getting rid of them.
        word = word.replace(x,"")
        #make sure that every input is completely uppercase so that checking
        #input doesn't have to worry about case sensitivity.
    return word.upper()

#returns a 0 or 1 value depending on whether the string is clean or not.
def is_clean(input_string):
    bad_chars = string.punctuation + string.whitespace + string.digits
    word = input_string
    error = 0 #this will be returned at the end, 1 means error (unclean), 0
    #means no error (clean)
    for x in bad_chars:
        if word.find(x) != -1:
            error = 1
            break
    return error

#construct functions takes two words, and constructs an alternad from them
def construct(word1, word2_lower):
    word2 = word2_lower.upper()
    constructed = "" #constructed word to be returned
    #program has 3 different scenarios depending on length of the words --
    #word1 is longer than word2, word2 is longer then word1, or word1 length
    #is equal to word2.
    if len(word1) == len(word2): #if the length of the words is equal
        for x in range(len(word2)): #run through length of either word
            constructed += word1[x] #add the current letter of word1
            constructed += word2[x] #then add the current letter of word2

    elif len(word1) > len(word2): #if word1 is longer than word2
        for x in range(len(word2)): #run through the shorter word
            constructed += word1[x] #add current letter of word1
            constructed += word2[x] #add current letter of word2
        constructed += word1[len(word2)] #finally, add the last letter of word1
        #to account for the shorter range which was adapted to account for
        #word2

    else: #if the length of word2 is longer than word1.
        for x in range(len(word1)): #run through the length of the shorter word
            constructed += word1[x] #add  current letter to word1
            constructed += word2[x] #add current letter to word2
    return constructed #return constructed word

#destruct function takes an alternad, and produces two words from it
def destruct(word):
    destructed_1 = word[::2]
    destructed_2 = word[1::2]
    return destructed_1, destructed_2 #return the words

#main -- accepts/cleans input and runs construct or destruct functions
def alternads():
    print("--------------ALTERNADS--------------")
    user_choice = clean(input("would you like to construct or destruct?: "))
    #takes cleaned user input as a variable

    #if the user doesn't enter construct or destruct, the choice is offered
    #until they do.
    while user_choice != "CONSTRUCT" and user_choice != "DESTRUCT":
        print("you didn't enter a valid choice.")
        #reassigns user_choice new, cleaned input.
        user_choice = clean(input("would you like to construct or destruct?: "))

    #given the choice to construct:
    if user_choice == "CONSTRUCT":
        print("--------------construct--------------")
        #takes two words for construct function, both cleaned.
        construct_word1 = input("enter a word to construct with: ")
        while is_clean(construct_word1) == 1:
            construct_word1 = input("not valid. enter a word to construct with: ")
        construct_word2 = input("enter another word to construct with: ")
        while is_clean(construct_word2) == 1:
            construct_word2 = input("not valid. enter a word to construct with: ")
        #prints the product of the function.
        print(construct(construct_word1, construct_word2))

    elif user_choice == "DESTRUCT":
        print("--------------destruct---------------")
        #takes one word for destruct function, cleaned.
        destruct_word = input("input word to destruct: ")
        while is_clean(destruct_word) == 1:
            destruct_word = input("not valid. enter a word to construct with: ")
        #technically runs the program twice, once for the first word, and once
        #for the second. i did this for formatting purposes, but i'm sure
        #there is a more efficient way to do ths.
        print(destruct(destruct_word)[0] + ", " + destruct(destruct_word)[1])

#run alternads
alternads()
