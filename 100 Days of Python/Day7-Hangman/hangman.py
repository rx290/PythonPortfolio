from random import randrange as randomizer
import  os, time, re


word_list = ["pills","bills","bill","gills","gill","drills","drill","dark"]

word = word_list[randomizer(0,len(word_list))]


stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',]

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
time.sleep(2)
os.system('clear')

blanks = []

for x in range(0,len(word)): 
    blanks.append('_') 
tries = 0
counter = 0
print(blanks)
print(stages[tries])



while(tries <= 6):
    if(tries ==6):
        print("You loose!")
        break
    else:
        user_input = input("Please Enter your desired character: ")
        def duplicates(lst, user_input):
            return [i for i, x in enumerate(lst) if x == user_input]
        if user_input in word and (word.count(user_input)<2):
            counter +=1
            index = word.find(user_input)
            blanks[index] = user_input
            print(blanks)
            print(stages[tries])
            if '_' not in blanks:
                print("you've won!")
                break
            time.sleep(1)
            os.system('clear')
        elif user_input in word and (word.count(user_input)>=2):
            indexer = duplicates(word,user_input)
            counter += len(indexer)
            for x in range(len(indexer)):
                blanks[indexer[x]] = user_input
                print(blanks)
                print(stages[tries])
                if '_' not in blanks:
                    print("you've won!")
                    break
                time.sleep(1)
                os.system('clear')
               
        else:

            tries +=1
            print("You've exhausted "+ str(tries) +" out of 6 tries.")
            print(stages[tries])
            time.sleep(1)
            os.system('clear')