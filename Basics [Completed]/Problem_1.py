"""If the marks obtained by a student in five different subjects are input through the keyboard,
find out the aggregate marks and perecentage marks obtained by the student. Assume that the maximum
marks that can be obtained by a student in each subject is 100"""

total_marks = 500
Subject_marks = []
for x in range(5):
    y = float(input("Please enter the marks for " + str(x+1) + " Subject: "))
    Subject_marks.append(y)
    

aggerate_marks = sum(Subject_marks)
percentage = (aggerate_marks / total_marks) * 100

# :.2f to show only 2 decimal places
print("You have attained {:.2f} out of {} which are equivalent to {:.2f}%.".format(aggerate_marks,total_marks,percentage))

## Revision 21st November 2025

max_marks_obtainable_per_subject = 100
subject=[
    'Maths', 'Physics','Chemistry','Computer Science','Biology'
]
marks = [    float(input("Please enter the marks for {} subject: ".format(x))) for x in subject  ]
obtained_marks = sum(marks)
print("Total marks obtained are: ",obtained_marks)
aggerate=  (obtained_marks/(max_marks_obtainable_per_subject*5))*100
print ("Your Aggregate is: ",aggerate,"%.")