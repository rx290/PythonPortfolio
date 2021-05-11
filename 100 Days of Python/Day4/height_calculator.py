heights = input("Please enter the heights of people: ")
new_list = heights.split(', ')
total = 0
for i in range((len(new_list))):
    total += int(new_list[i])

avg_height = total / len(new_list)
print(avg_height)