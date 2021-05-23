from random import randrange as randomizer

word_list = ["pills","bills","bill","gills","gill","drills","drill","dark"]

word = word_list[randomizer(0,len(word_list))]
print(word)
blanks = []

for x in range(0,len(word)): 
    blanks.append('_') 

print(blanks)



tries = 0
for i in range(0,6):
    user_input = input("Please Enter your desired character: ")
    if user_input in word:
        index = word.find(user_input)
        blanks[index] = user_input
        print(blanks)
    else:
        tries +=1
        print("You've exhausted {tries} out of 6 tries.", tries)