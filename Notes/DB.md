# Database Notes

## Create Clause

This clause is used to either create Database or tables examples are as follows:

1. IF NOT Exist Create Database School;
2. IF NOT Exist Create Table Student (Primary_key Auto Increment Integer id, varchar(50) fullName, varchar(50) address );

## Select Clause

Use select clause to select items from Database, examples are as follows:

1. Select * from Student;
2. Select distinct fullName from Student;
3. Select * from Student order by id DESC;

## Where Clause

Where Clause is used when we are searching for certain things but the query is not dependent upon some Arithmetic and Logical Conditions examples:

1. Select * from Student where address = "Street 12 Sector C Lahore";
2. Select * from Student where Not fullName = "Ali";
3. Select * from Student where id = 32;
4. Select * from Student where not id = 32 and fullName = 'Ali';
5. Select * from Student Where address = "Street 12 Sector C Lahore" or address = "Street 12 Sector C Karachi";

## Order By

This clause is a conditional statement to sort search results accordingly either by ascending order or by descending order, examples:

1. Select * from Student order by id DESC;
2. Select * from Student order by fullName;
3. Select * from Student order by fullName, id;

## Insert Clause

This clause is used to insert data into tables, examples:

1. Insert into Student (fullName, address) values ('Rawan Teja', "Street 12 Sector C Lahore");

## NULL handling

This is to handle null safety and empty entries, example:

1. Select * from Student where address is NULL;
2. Select * from Student where address is Not Null;

## Update Clause

This clause is used to update an entry stored in a table example:

1. Update Student set address = '12 Street Sector D Lahore';
2. update Student set fullName = 'Ali Mehra' where id = 12;
3. Update Student set fullName = 'Ali Mehra', address = " " where id = 12;

## Delete Clause

This Clause is used to delete the item from the table example:

1. Delete from Student;
2. Delete from Student where id = 2;

## SQL Functions

These built in functions are used to manipulate data according to users need. Examples:

1. Select Min(Salary) from Employees;
2. Select Max(Price) from Products;
3. Select Count(*) From Products Where Price = 18;
4. Select Avg(Price) From Products;
5. Select Sum(Price) from Products;

