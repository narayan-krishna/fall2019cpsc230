import random
from itertools import permutations

#these two lists contain all halloween words for unscrambling -
#i separated them so that they wouldn't be too long on one line
halloween_words_one = ["spooky", "ghost", "tombstone", "pumpkin", "murder", "cobweb", "dusty", "skeleton", "costume", "candy"]
halloween_words_two = ["blood", "creepy", "witch", "spider", "haunted", "goosebumps", "scary", "scream", "terror", "decorations"]

#the two lists are brought back together here
halloween_words_total = halloween_words_one + halloween_words_two

#quick introduction to the game
print("----------you are playing the halloween game----------")
print("--------------unscramble the word to win--------------")
print("-----------------you have three tries-----------------")
print("----------------you have a max 5 plays----------------")
print("")

quit = 0 #tracks whether or not the user would like to quit the game, or if the user
#hits a negative score, in which case the game quits automatically ("game over!")
total_score = 0 #tracks total score over multiple games -- if the player correctly
#guesses the word, adds 1 to the score, if not, takes 1 away from score. again,
#if score is negative, then the game automatically quits.
while quit == 0: #while the score is not negative and user has not chosen to quit
    #word_choice is a word chosen at random from the total list of words.
    word_choice = halloween_words_total[random.randint(0, len(halloween_words_total)-1)]
    #permutation is a list of all possible permutations of the chosen word. the
    #permutations function exists through itertools
    permutation = list(permutations(list(word_choice)))
    #permutation_choice_list is a randomly chosen permutation from the permutation
    #list -- this exists as a list
    permutation_choice_list = permutation[random.randint(0, len(permutation)-1)]
    #choice_str is whatever the choice from the permuation list was, joined together.
    #this way, our permutation choice is a string and can be printed as such.
    choice_str = "".join(permutation_choice_list)

    #print the word required to unscramble
    print("the word to unscramble is: " + choice_str.upper())
    count = 0 #turn counter
    while count != 3: #while the user has not used their third turn
        guess = input("enter your guess>> ") #takes in guess
        if guess.lower() == word_choice: #if guess is correct
            #print their success, print the correct word.
            print("you've won! the correct word was indeed " + word_choice.upper() + ".")
            total_score += 1 #add 1 to the total score
            break #end the loop, and start with another word.
        else:
            count += 1 #if guess is wrong, add 1 to the turn counter
    if count == 3: #if the loop is broken AND the counter is 3, the user has lost.
        #print loss, print correct word
        print("YOU LOSE. the correct word was " + word_choice.upper() + ".")
        #take 1 away from total score.
        total_score -= 1

    print("your total score is " + str(total_score) + "!") #print total score
    if total_score < 0: #if the score, is negative, game ends.
        print("GAME OVER!")
        quit = 1 #set game to quit
    elif total_score == 5:
        print("you've used all 5 plays! you've reached the max score of 5.")
        print("thank you for playing!")
        quit = 1
    else:
        keep_playing = input("would you like to keeping playing? enter y or n: ").lower()
        if "n" in keep_playing: #if they say n, quit game
            print("your final score was " + str(total_score) + ".")
            print("thank you for playing!")
            quit = 1 #set game to quit

        #if answer doesn't have an n, the game continues

    print("------------------------------------------------------")
