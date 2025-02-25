# Postgres SQL

## Commands

    Here is a list of all commands one would require to work with Postgres SQL
    1.  psql --username= user_name --dbname= db_corpus eg:
    psql --username=freecodecamp --dbname=postgres : used to login to the postgreSql
    2. \l : List all the databases list in the Postgres SQL.
    3. CREATE DATABASE database_name; : Creating a database in the PostgreSQL server
    4. \c database_nam : used to connect to the database
    5. \d : used after connecting to the db List all the tables
    6. CREATE TABLE table_name(); : used to create table
    7. \d name : name can be replaced with table name to list the entire table.
    8. ALTER TABLE table_name ADD COLUMN column_name Column_type; : This command lets you add columns/attributes to the table.
    9. ALTER TABLE table_name Drop COLUMN (column_name); : This command lets you remove/drop columns/attributes from the table.
    10. ALTER TABLE table_name RENAME COLUMN column_name TO new_name; : used to rename column/attribute name
    11. INSERT INTO table_name(column_1, column_2) VALUES(value1, value2); : used to add row or record into the table
    12. SELECT columns FROM table_name; : to view selected column.
    13. SELECT * FROM second_table; to select all the columns from a target table
    14. DELETE FROM table_name WHERE condition; to delete a record when it meets a condition
    15. DROP TABLE table_name; : is used to drop a table
    16. ALTER DATABASE database_name RENAME TO new_database_name; change database name
    17. DROP DATABASE second_database; is used to drop database
    18. UPDATE table_name SET column_name=new_value WHERE condition; to update a table
    19. SELECT * FROM table_name ORDER BY column_name; for sorting
    20. ALTER TABLE table_name ADD PRIMARY KEY(column_name); for adding primary keys
    21. ALTER TABLE table_name DROP CONSTRAINT constraint_name; used for dropping constraints
    22. ALTER TABLE table_name ADD COLUMN column_name DATATYPE REFERENCES referenced_table_name(referenced_column_name); setting up a foreign key
    23. ALTER TABLE table_name ADD UNIQUE(column_name); to use distinct property
    24. ALTER TABLE table_name ADD UNIQUE(column_name); altering attributes/columns
    25. CREATE TABLE table_name(column_name DATATYPE CONSTRAINTS); quicker consise way of adding columns
    26. Use junction object to create Many to many relati
    27. ALTER TABLE table_name ADD PRIMARY KEY(column1, column2); : COmposite key
    28. SELECT columns FROM table_1 FULL JOIN table_2 ON table_1.primary_key_column = table_2.foreign_key_column; full join
    29. select * from characters full join sounds on characters.character_id = sounds.character_id; one to one
    30. SELECT columns FROM junction_table
        FULL JOIN table_1 ON junction_table.foreign_key_column = table_1.primary_key_column
        FULL JOIN table_2 ON junction_table.foreign_key_column = table_2.primary_key_column;

        Many to Many
