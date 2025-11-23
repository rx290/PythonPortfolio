"""Write a program which takes a number uas input from the user and displays whether its palindrome
or not? A palindrome is a number that remains the same when its digits are reserved"""



try:
    number = int(input('Please enter some number: '))
    print("num:", number)
    number =str(number)
    if number == number[::-1]:
        print("The number is palindrome")
    else:
        print("The number is not palindrome")
except ValueError:
    print("Please input integer only...") 