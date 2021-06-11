import random
import time
import os

def greeter():
    print("Welcome to Number Guessing Game")
    print("You've to guess a number between 1 - 100")
    print("There are two mode from which you have to choose 'easy' and 'hard'")
    choice = input("Please enter your choice: ")
    return choice

def guesser(choice):
    
    
    num = random.randrange(1, 100)
    if choice == 'easy':
        _lives = 10
        while _lives >0:
            c= int(input("You've "+ str(_lives) + " remaining. \nGuess your number: "))
            if num - c >= 5:
                print("Too High!")
                _lives = _lives - 1
            elif num == c:
                print("You've guessed the right number!")
                break
            else:
                print("Too Low!")
                _lives = _lives - 1
    elif choice == 'hard':
        lives = 5
        while lives >0:
            c= int(input("You've "+ str(lives) + " remaining. \nGuess your number: "))
            if num - c > 5:
                print("Too High!")
                lives = lives - 1
            elif num == c:
                print("You've guessed the right number!")
                break
            else:
                print("Too Low!")
                lives = lives - 1
    else:
        print("Invalid entry")
        time.sleep(2)
        print("Restarting the script")
        os.system("clear")
        guesser(greeter())
                
if __name__ == '__main__':
    guesser(greeter())