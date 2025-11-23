age = int(input("Please enter your age: "))
days, week, months = (90-age)*365 , ((90-age)*52) , ((90-age)*12)
print("You have {days}, {weeks} weeks and {months} months left.".format(days= days, weeks = week, months = months))