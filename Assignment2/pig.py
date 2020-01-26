#Krishna Narayan
#2327205
#narayan@chapman.edu
#CPSC 230 section 08
#Assignment 2

import random

player_score = 0
computer_score = 0

turn = 0 #uses this value to figure out whose turn it is
while player_score < 100 and computer_score < 100: #main game cycle starts here
    if turn == 0: #players turn
        print("---------player's turn---------")
        turn += 1 #now that it is the players turn, changes the turn counter
        #approriately so that the next turn is computers

        #print statements to show state of game
        print("player score: " + str(player_score)) #prints player score
        print("computer score: " + str(computer_score)) #prints computer score

        turn_score = 0 #keeps track of the points earned during this specific
        #turn

        #take user input for choice to roll or hold
        player_input = input("would you like to roll (r) or hold (h)? ")

        #if the player chooses to roll, run random number generator.
        while player_input == "r":
                roll = random.randint(1,6)
                if roll == 1:
                    #ends the cycle -- moves to computers turn.
                    print("your roll was 1. you receive 0 points.")
                    break
                else:
                    #adds roll to turn score
                    turn_score += roll
                    #makes player aware of temporary score
                    print ("your roll was a " + str(roll) + ", your potential score is " + str(player_score + turn_score))
                    #continues to cycle by asking for another input
                    player_input = input("would you like to roll (r) or hold (h)? ")
                    #resets the loop
                    continue
        #if player chooses to hold
        if player_input == "h":
            #add turn score to actual score
            player_score += turn_score
            print("player score: " + str(player_score))
            #if the player has more than 100 points after holding, the game
            #is over.
            if player_score >= 100:
                print("victory!")
                break

    if turn == 1: #computers turn
        print("---------computer's turn---------")
        turn -= 1 #now that it is the players turn, changes the turn counter
        #approriately so that the next turn is computers

        turn_score = 0 #keeps track of the points earned during this specific
        #turn

        #once the computer hits turn score of 20, the computer holds. so only
        #run the roll process while the turn score is less than 20
        while(turn_score < 20):
            #generate a number
            roll = random.randint(1,6)
            #again, end the process entirely if the roll is 1. it then becomes
            #players turn.
            if roll == 1:
                print("computer has rolled a 1. it received 0 points.")
                break
            else:
                #if roll is not a 1, add roll to turn score. if the potential
                #score of the computer is 100 or greater, the computer holds
                #to achieve victory.
                turn_score += roll
                print ("computer has rolled a " + str(roll))
                #here is where the computer holds if victory can be achieved.
                if computer_score + turn_score >= 100:
                    print("computer has decided to hold.")
                    print("the computer has won.")
                    break

        #if the computer has achieved a turn score higher than 20, and can't
        #achieve victory, the computer's turn score is added to the actual score
        # and the computer holds. it becomes the players turn.
        if (turn_score >= 20 and computer_score + turn_score < 100):
            computer_score += turn_score
            print("computer has decided to hold.")
            print("computer score: " + str("computer score"))
