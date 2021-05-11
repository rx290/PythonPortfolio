import  string
import  random

content = string.ascii_letters + string.punctuation +string.digits

password = ''

length = int(input("Please enter password length: "))

for i in range(length):
    password += content[random.randrange(0,len(content))]

print(password)