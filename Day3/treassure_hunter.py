import time
print("Welcome to Treassure island \n Your mission is to find the treassure")

choice = input("Do you want to go right? or left?").lower()
if choice == 'left':
    print("You kept walking left!")
    time.sleep(3)
    print("A lake is in sight what would you do?")
    action = input("swim or wait?: ").lower()
    if action == 'wait':
        print("You've decided not to swim!")
        time.sleep(1)
        print("you waited for a bit! and started walking arbitrarily")
        time.sleep(3)
        print("Three doors appear, Red, Blue and Yellow.")
        choose = input("Which one are you going to choose?:").lower()
        if choose == 'red':
            print('you choose the red door. it was hard to open, but now it is open.')
            time.sleep(3)
            print('you started walking inside and air is getting hotter!')
            time.sleep(3)
            print("it is pitch black now but you kept on walking and suddenly a bright light hit you and you're free falling in a fire pit.")
            time.sleep(3)
            print("Game Over!")
        elif choose == 'yellow':
            print("The Door was pretty Stuck but you managed to open it up.")
            time.sleep(3)
            print("You tripped over! is that a skeleton you screamed!")
            time.sleep(2)
            print("you realized the purple pirate hat! and you know for sure you've found the lost treasurer of captain jones")
            print("You win!")
        else:
            print('you choose the blue door. it was pretty easy open, but you were greeted by no mads.')
            time.sleep(3)
            print('They had beaten you down and cooked you as supper')
            time.sleep(3)
            print("Game Over!")
    else:
        time.sleep(3)
        print("You started swiming.")
        time.sleep(3)
        print("Something is dragging you down!")
        time.sleep(3)
        print('it is a shark!, that is the last thing you will ever see!\nGame Over!')

else:
    print("Fell into a hole!\nGame Over.")