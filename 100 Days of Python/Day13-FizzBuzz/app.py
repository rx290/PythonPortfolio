num = int(input("Please enter a number to check FizzBuzz: "))

if num%3 ==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif  num%5==0:
    print("Buzz")
else:
    print(num," ain't divisible by 3 or 5")
