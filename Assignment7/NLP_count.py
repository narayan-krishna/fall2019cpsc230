#Krishna Narayan
#2327205
#narayan@chapman.edu
#CPSC 230 section 08
#Assignment 7

import string
import operator

#removes all punctuation from a string
def removed_punctuation(str):
    for x in string.punctuation: #runs through individual characters of punctuation string
        str = str.replace(x, "") #replaces punctuation with nothing
    return str #return the string

#reads a file, and converts contents to a string
def read_file(file_name):
    return_string = "" #set up a string that we can add the read file to
    input_file = open(file_name, 'r') #open up the file
    for x in input_file: #for lines in the file,
        return_string += x #add them to the string set up earlier
    return return_string #return the string
    input_file.close() #close the file

def build_dictionary(string):
    lower_string = string.lower() #convert the string to lower case so we don't get the same word twice
    word_list = lower_string.split() #split up the words of the string, make them a list

    for x in range(len(word_list)): #run through the list by index
        word_list[x] = removed_punctuation(word_list[x]) #replace every word with its non-punctuated counterpart
    dictionary = {} #set up a new dictionary
    for x in word_list: #run through the word list
        if x in dictionary: #if the word is already in the dictionary,
            dictionary[x] += 1 #add 1 to the occurence value
        else:
            dictionary[x] = 1 #otherwise set it up in the dictinoary with an occurencce value of 1

    return dictionary #return the dictionary

#sort and write a dictionary onto a given file
def write_file(dictionary, output_file):
    out_file_words = open("word_list", 'w') #create a new file
    print("[WORD] ---------- [# OF USES]", file=out_file_words) #file guide
    sorted_list = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True) #sort the list.
    #reverse makes it so that the list is sorted by value in descending rather than ascending order.
    for k,v in sorted_list: #for eveyr key and value
        #print them to file
        print(k + " ---------- " + str(v), file=out_file_words)
    #close the file
    out_file_words.close()

#write a built dictionary to a file. the dictionary is built from a given text
write_file(build_dictionary(read_file("hp.txt")),"out.txt")
