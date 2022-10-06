"""
Create a structure to specify data on students given below:

Roll number, Name, Department, Courses, Joining_Year.

Assume that there are 450 students in total.

Write a function to print names of all students who joined in a particular year,
write a function to print information of the student whose roll number is given.
"""
students_data = {'Student Number': {'Roll Number':'Some Integer or Alpha Numeric Value','Name':"Full Name",'Department':"Department Name",'Courses':"Courses",'Joining_Year':"Joining Year" }}
def add_data(key:int,value:dict):
    students_data[key] = value
    
def all_records(collection:dict):
    for keys, values in collection.items():
        print(keys,':',values)
        
add_data(1,{'Roll Number':'01','Name':"Asad Waseem",'Department':"Computer Science",'Courses':"NLP, ML, DL",'Joining_Year':"2020" })
all_records(students_data)