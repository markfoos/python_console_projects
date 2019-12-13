#Guess my number game with some console visuals
#Created by Mark foos
#Inspired by M. Barnes original script

#imports
import sys

#main function
def game_init():
    play = input("Press Enter to Start\n")

    if str.lower(play) == 'exit':
        print("\nGoodbye!")
    else:
        print("Welcome to Guess My Number")
        print("-" * 82)
        from random import randint
        answer = randint(0,10)
        guessed = False
        guesses = 0
        print("There is a radom number between 0 and 10 for you to guess")
#create this array for imagery
        guess_Array = [1,2,3,4,5,6,7,8,9,10]
        print("-" * 82)
        for i in guess_Array:
            sys.stdout.write("|   " + str(i) + "   ")

            sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.flush()
        print("-" * 82)
#main while loop
        while not guessed:
            try:
                guess = int(input("\n\nEnter your guess\n"))
#enumerate array for imagery
                for n, i in enumerate(guess_Array):
                    if i == guess:
                        guess_Array[n] = "X"
#show image
                print("-" * 82)
                for i in guess_Array:
                    sys.stdout.write("|   " + str(i) + "   ")

                    sys.stdout.flush()
                sys.stdout.write("\n")
                sys.stdout.flush()
                print("-" * 82)
                guesses += 1
            except:
                print("\nEnter a valid number")
                continue
            if guess == answer:

                print("\n\nYou've guessed it in " + str(guesses) + " tries, the number was {}.".format(answer), "BOOM!")
                guessed = True
                break
            elif guess in range(0,11) and guess > answer:
                print("'To the LEFT, To the LEFT'")
                continue
            elif guess in range(0,11) and guess < answer:
                print("'To the RIGHT, To the RIGHT'")
                continue
            elif guess == 99:
                guessed == True
                break
            else:
                print("\nNumber between 1 and 10")
                continue


game_init()

#keep playing loop
continue_playing_loop = True
while continue_playing_loop == True:
    print("\n\nPlay Again? Enter 'yes' or 'no'")
    play_again = str.lower(input())
    if play_again == 'yes':

        game_init()
    else:
        exit()
