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
    19. 