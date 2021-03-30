name1 = input("Please Enter Full Name:").lower()
name2 = input("Please Enter Full Name:").lower()

combined = name1 +" " + name2
l1 = ['t','r','u','e']
l2 = ['l','o','v','e']

l1_count = 0
l2_count = 0

for i in range(len(l1)):
    l1_count += combined.count(l1[i])

for j in range(len(l2)):
    l2_count += combined.count(l2[j])

total_count = str(l1_count)+str(l2_count)

if int(total_count) <10 and int(total_count)>90:
    print("Your Score is " + total_count +",you go together like coke and mentos.")
elif int(total_count) >40 and int(total_count)<50:
    print("Your Score is " + total_count +",you are alright together.")
else:
    print("Your Score is " + total_count)