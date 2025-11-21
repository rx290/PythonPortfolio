"""If a five digit number is input through the keyboard, write a program to print a new number by adding one to each of its digits.
For example if the number that is input is 12391 then the output should be displayed as 23402"""

num = input("Please enter a five digit number: ")

new_num = ""
if len(num) == 5:
    for i in num:
        new_num = new_num + str(int(i)+1)
    print("Entered number was {}.\nNew Number is {}.".format(num,new_num))
else:
    print("Please enter 5 digit number")

