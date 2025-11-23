"""
An insurance company has following rules to calculate premiums:

a. if a person's health is excellent and the person is b/w 25 and 35 years of age
   and lives in a city and is a then the premium is $4 per thousand and his policy amount
   can't exceed 200,000$

b. if a person satisfies all the above conditions except that the sex is female then the premium is 3$
   per thousand and her policy amount cannot exceed 100,000$

c. if a person's health is poor and the person is b/w 25 and 35 years of age and lives in a village and is a male or a female
then the premium is $6 and his policy cannot exceed $10,000

d. if a male fulfils a but is in village their premium is 3.5$ and can't exceed 150,000 policy amount.

e. if a female fulfils b but is in village their premium is 2.5$ and can't exceed 75,000 policy amount

f. in all other cases the person is not insured

write a program to output whether the person should be insured or not, his/her premium rate and maximum amount for which he/she can be insured.
"""
age = int(input("Please enter your age:"))
gender = input("Please enter your gender (male/female): ")
income = float(input("Please enter your monthly income:"))
residence = input("Please enter whether you live in a city or village: ")
health = input("Please enter the Statue of your health (excellent/poor): ")

male_policy, female_policy, poor_health, male_village, female_village = 200000,100000,10000,150000,75000
male_rate,female_rate,poor_health_rate, mv_rate,fv_rate = 4,3,6,3.5,2.5

if age >= 25 and age<=35:
   if residence == "city":
      if health=="excellent":
         if gender == "male":
            print("You are eligible to get insured, at a premium rate of {}$ per thousand and your policy can't exceed {}".format(male_rate,male_policy))
         else:
            print("You are eligible to get insured, at a premium rate of {}$ per thousand and your policy can't exceed {}".format(female_rate,female_policy))
      else:
         print("You are eligible to get insured, at a premium rate of {}$ per thousand and your policy can't exceed {}".format(poor_health_rate,poor_health))
   else:
      if gender == "male":
         print("You are eligible to get insured, at a premium rate of {}$ per thousand and your policy can't exceed {}".format(male_village,mv_rate))
      else:
         print("You are eligible to get insured, at a premium rate of {}$ per thousand and your policy can't exceed {}".format(female_village,fv_rate))
else:
   print("You're illegible for insurance.")