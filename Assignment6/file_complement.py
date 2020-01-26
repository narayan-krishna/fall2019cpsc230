#Krishna Narayan
#2327205
#narayan@chapman.edu
#CPSC 230 section 08
#Assignment 6

import string #import so that we can test the characters of the input

#Complement function
def complement(sequence):
    alphabet_one = "ACTG " #alphabet of letters
    alphabet_two = "TGAC " #complement to that alphabet
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

chosen_file = input("enter input file: ") #enter a file to read
try: #set up excpeption system, so that if an exception is thrown, we can
#print an approriate message
    input_file = open(chosen_file, 'r') #open the file chosen to be read
    out_file_complement = open("results_complement.txt", 'w') #write a new file
    #with the complements of the sequences
    out_file_reverse = open("reverse_complement.txt", 'w') #write a new file
    #with the reverse complements of the sequnces

    for sequence in input_file: #run through the lines (sequences) of the file
        stripped = sequence.strip() #get rid of extraneous whitespace before or
        #after the string
        if is_clean(stripped) == 0: #if the stripped sequence is clean:
            #print complement onto file
            print(complement(stripped), file = out_file_complement)
            #print reverse complement onto file
            print(rev_complement(stripped), file = out_file_reverse)
        else:
            #print that the sequence was invalid to both files
            print("this sequence was invalid.", file = out_file_complement)
            print("this sequence was invalid.", file = out_file_reverse)

    #close all three files that we are working with
    input_file.close()
    out_file_complement.close()
    out_file_reverse.close()

#if we run into the FileNotFoundError error, print the approriate message
except FileNotFoundError:
    print("the file entered does not exist")
