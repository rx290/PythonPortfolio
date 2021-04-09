# Database Notes

## Database General

1. Create Database testDB;
2. Drop Database testDB;
3. Drop Table Student;
4. Turncate table Person;
5. Alter Table Person Add Birthday Date;
6. Alter Table Person Drop Column Birthday;

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

## Like Clause

This is a clause to use RE like methods to fetch abstracted data, examples

1. Select * from Students where fullName like "a%";
2. Select * from Students where fullName like "%a";
3. Select * from Students where fullName like "%a%";
4. Select * from Students where fullName like "a%b";
5. select * from Students where fullName Not like "a%";

## WildCards

These clauses are used with like to attain more arbitrary results, example:

1. Select * from Student where address Like '_a%';
   1. To Select any address which has a as the second character of first word
2. Select * from Student where address Like '[acs]%';
   1. Select all from students where address is either starting with a, c or s
3. Select * from Student where address Like '[a-f]%';
   1. Select all from students where address is either starting from a and going towards f
4. Select * from Student where address Like '[!acf]';

## In clause

In clauses are used when one have to iterate through some sort of parenthesis having multiple values, example:

1. Select * from Student where City in ('Karachi','Lahore','Islamabad');
2. Select * from Student where City Not in ('Wazirabad', 'HafizaBad', 'Lailpur');

## Between Clause

This is a range finder of sql example:

1. Select * From Products where prices Between 10 and 20;
2. Select * From Products where prices Not Between 10 and 20;
3. Select * From Products where fullName Between 'Ali' and 'Farhan;

## Alias Clause

This clause is used to give nickname to views, tables and fetched data eg:

1. Select fullName from Student as Names;
2. Select * from Student as DayScholars;

## join Clause

A clause which is used to combine rows from two or more than two tables, based on related / mutual table between them.

There are fours types of joins which are as follows:
    1. Left Join (Returns all records of the left table, and only mutual or matched records from right table)
    2. Right Join (Returns all records of the Right table, and only mutual or matched records from left table)
    3. Inner Join (Returns mutual records having same values)
    4. Outer Join (Return all records where there is a mutual / matched value of either table)

examples:

1. Select * from Orders left join Customers on Orders.CustomerID = Customers.CustomerID;
2. Select * From Orders Inner Join Customers on Orders.CustomerID = Customers.CustomerID;
3. Select * from Orders Right Join Customers on Orders.CustomerID = Customers.CustomerID;

## Group By

It groups two or more than two rows, examples:

1. Select * count(CustomerID), Country from Customers group by Country;
2. Select * count(CustomerID), Country from Customers order  by Country Order by count(CustomerID) DESC;

## Most common Interview Questions

1. What is RDBMS?
2. What are records?
3. What are advantages of RDBMS?
4. What is Data Redundancy?
5. What are Database Relationships?
   1. 1 - 1
   2. 1 - many
   3. many - 1
6. Explain Normalization and De-normalization?
7. Why is indexing used?
8. Types of SQL Statements?
   1. DDL: Data Definition Language
   2. DML: Data Manipulation language
   3. DCL: Data Control Language
9. State DDL , DML and DCL Clauses?
   1. DDL
       1. Create
       2. Alter
       3. Truncate
       4. Drop
       5. Rename
   2. DML
      1. Insert
      2. Update
      3. Delete
      4. Merge
   3. DCL
      1. Commit
      2. Rollback
      3. Savepoint
10. Difference between Having and Where Clause?
11. Explain Indexing and its purpose?
12. What are views?
13. What are cursors and its type?
14. What are database transactions?
15. What are database lock?
16. Define Joins and explain its types?
17. What are aggregated functions?
18. What are keys?
19. Difference between delete and truncate and drop?
20. What is normalization and its types?
21. Find Second Highest Salary?
    1. Select Max(salary) from employee order by salary DESC n-1, 1;
