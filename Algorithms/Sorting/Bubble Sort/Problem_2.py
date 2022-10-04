"Write a Python program to sort unsorted numbers using Recursive Bubble Sort." 
sample =[14, 21, 27, 41, 43, 45, 46, 57, 70]

def sorter(sample:list):
    choice = input("Please enter how you want your list to be sorted:\n1. Ascending Order\n2. Descending Order\nYour Choice: ")
    if choice == '1':
        for i in range(len(sample)-1,0,-1):
            for j in range(i):
                if sample[j] >= sample[j+1]:
                    sample[j],sample[j+1] = sample[j+1],sample[j]
    elif choice == '2':
        for i in range(len(sample)-1,0,-1):
            for j in range(i):
                if sample[j] <= sample[j+1]:
                    sample[j],sample[j+1] = sample[j+1],sample[j]
    else:
        print("Invalid Choice!")
    return print(sample)

sorter(sample)