# Bash

    To print something on the terminal use "eco" command.
    example:
        echo hello world.

    To create anything you can use "touch" command.
    example:
        touch filename.file_extension
        touch notes.md

    you can use "cd" to change directory.
    example:
        cd .. to change the current directory one step
        cd ../.. to change the current directory two steps
        add more ../ to the cd command to change the steps it can change the directory.

    ls command is used to get the list of all the items in the directory
    example:
        pc: /some_directory$ ls
    There are many other use-cases for list/ls command for example
    ls -l is used to list down all the permissions a directory has.
    here is a table for permission set:

        |symbol | Meaning   |
        |x      |Execute    |
        |r      |Read       |
        |w      |Write      |
        |rw     |Read Write |


    To update the permission we use chmod command
    example:
        chmod +x hello.sh

    we can use sh command to execute a script this sh is short for shell
    example:
        you have a script stored called hello.sh which eco hellow world
        you simply need to execute this command pc: /some_directory$ sh hello.sh

    To know what location or which program/interpreter is running you need "which" keyword.
    example:
        which bash

    There is something called shebang which is the absolute path to the bash i.e. #!/bin/bash and you will be seeing shebang at the top of every script.
    example:
        #!/bin/bash
        echo hello bash

    you may ask why adding shebang at the top right?
    well it makes your script executable and by adding ./ in front of your script and that's all you need to execute the script.
    

    There is another concept of variables in scripting, you need 


    There is a tag called --help for any commands to get more information about it, but it that don't work use "man" keyword.
    example:
        man echo
        ls --help

    Conditional statement
        if [[ statement ]] #note that the spaces are compulsory
        then
            statements
        else
            statements
        fi #ending statement


    Logical expressions
        -eq equals
        -lt less than
        -gt greater than
        -ge greater than equal to
        -le less than equal to
        =~ string to right would be evaluated against an RE
        == string pattern equal matching
        != string not equal to pattern matching
        && AND Gate
        || OR GATE


    