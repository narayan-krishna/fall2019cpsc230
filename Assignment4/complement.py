#Krishna Narayan
#2327205
#narayan@chapman.edu
#CPSC 230 section 08
#Assignment 4

import string #import so that we can test the characters of the input

#Complement function
def complement(sequence):
    alphabet_one = "ACTG" #alphabet of letters
    alphabet_two = "TGAC" #complement to that alphabet
    comp = "" #variable complement which we will return
    for x in sequence: #run through the given sequence
        index_alpha_one = alphabet_one.find(x) #find where the character is the
        #first alphabet
        comp += alphabet_two[index_alpha_one] #plugging in this index into the
        #second index will give the complement of
    return comp #return the complement

def rev_complement(sequence):
    rev_sequence = sequence[::-1] #reverse the sequence given

    return complement(rev_sequence) #returns the complement of reversed
    #reversed sequence

#returns a 0 or 1 value depending on whether the string is clean or not.
def is_clean(input_string):
    bad_chars = string.punctuation + string.whitespace + string.digits + "BDEFHIJKLMNOPQRSUVWXYZ"
    word = input_string
    error = 0 #this will be returned at the end, 1 means error (unclean), 0
    #means no error (clean)
    for x in bad_chars:
        if word.find(x) != -1:
            error = 1
            break
    return error

sequence = input("insert sequence: ").upper() #takes in the sequence
while is_clean(sequence) == 1: #if the sequence is not clean (has anything that
    #isnt A, T, G, or C, then ask for sequence again
    sequence = input("you entered an invalid sequence. try again: ").upper()
choice = input("complement or reverse complement (C or R): ").upper() #takes in
    #a choice as to which function should be used
while choice != 'C' and choice != 'R': #if the choice isn't the letter c or r,
    #ask for choice again
    choice = input("you didn't enter a valid choice. try again: ").upper()
if choice == "C": #if the choice is c, run complement
    print("the complement is " + complement(sequence))
elif choice == "R": #if the choice is r, run reverse complement
    print("the reverse complement is " + rev_complement(sequence))
