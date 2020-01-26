#Krishna Narayan
#2327205
#narayan@chapman.edu
#CPSC 230 section 08
#Assignment 4

import string

#translates a given word to pig latin.
def word_to_pig(word):
    consonants = "bcdfghjklmnpqrstvwxyz" #list of constants for recognization
    vowels = "aeiou" #list of vowels for recognization
    consonant_end = 0 #setting a variable for where a vowel is found in a string
    #, or where the consonants end
    if word[0] in consonants: #if the first letter is a consonants
        starting_consonants = "" #create a string that will be a string of the
        #starting consonants of the word, or the consonants until a vowel is
        #found
        for x in word: #run through the word
            if x in vowels: #check to see if x is a value
                consonant_end = word.find(x) #set consonant_end to index of
                #found vowel
                break
            starting_consonants += x #otherwise keep adding consonants to the
            #starting_consonants string
        to_return = word[consonant_end:] + starting_consonants + "ay" #finally,
        #return the word excluding the starting consonants + the starting
        #consonants + ay
        return to_return[0].upper() + to_return[1:] #make the first letter caps
    elif word[0] in vowels: #if word starts with a vowel
        return word[0].upper() + word[1:] + "yay" #return, with a first letter
        #caps, the normal word + yay at the end

#convert a full name into two separate names
def full_name_conversion(full_name):
    space_index = full_name.find(" ")
    if space_index == -1:
        return "0", "0"
    else:
        first_name = full_name[:space_index]
        last_name = full_name[space_index + 1:]
        return first_name, last_name

#convert a full name into pig latin
def name_to_pig(first_name, last_name):
    return word_to_pig(first_name) + " " + word_to_pig(last_name) #use the word
    #to pig function translate names separately, then combine

#given a string, ensure that the input is clean
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

insert_name = input("please insert a name: ").lower() #take a full name
first_name = full_name_conversion(insert_name)[0] #isolate the first name using
#the full name conversion function
last_name = full_name_conversion(insert_name)[1] #isolate the second name using
#the full name conversion function
while is_clean(first_name) == 1 or is_clean(last_name) == 1: #while the input
#isn't clean, or no space is found in the name, ask for the name again, convert
#this name again.
    insert_name = input("please insert a valid name: ").lower()
    first_name = full_name_conversion(insert_name)[0]
    last_name = full_name_conversion(insert_name)[1]

#run the name through the name to pig function
print(name_to_pig(first_name, last_name)) #prints
