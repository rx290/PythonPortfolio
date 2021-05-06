# OOP

1.  What is encapsulation?
    The attribute of an object to hide the data and set access specifiers for it is known as encapsulation.
        Access specifers are of three types which are as follows:
            1. Public 
            2. Protected
            3. Private

2.  What is polymorphism?
    The attribute to exist in multiple forms is known as polymorphism. as per object attribute it means having multiple definitions 
    of a method.
    Types:
        1. Static (occurs at compile time i.e. method overloading)
        2. Dynamic (occurs at runtime i.e. method overriding)

3. What is method overloadding and overriding?
    Method overloading:
        Creating metods of same name but with diffrent arguments.

    Method overriding
        A feature to redefine the base class methods as per the child class need but the signature meaning, argument passed and return type will remain same.

4. What is inheritance?
    The concept where one class can share its structure and behavior to another class is called inheritance.
    there are several types of inheritance which are as follows:
        1. Signle inheritance
        2. Multiple inheritance
        3. Multilevel inheritance
        4. Hybrid inheritance

5. What is data abstraction?
    Hiding of implementation details and displaying only relevant information is known as data abstraction.
    Data abstraction techniques:
        1. Abstract Class
        2. Abstract Methods

    Abstract class consist of abstract methods and these methods are declared but not defined if these methods are to be used in any subsclass then these methods needs to be exclusively defined in that subclass

6. virtual functions?
    These are defined in the parent class with virtual keywords and are overriden in the subclass these are used to achieve runtime polymorphism.
    
7. What are access specifiers and why they're used?
    access modifiers / specifiers are basically attributes of a class which determines the access scope of its methods or variables.
    Types of access specifiers are as follows:
        1. Public
        2. Default
        3. Private
        4. Protected
        5. Friend
        6. Protected Friend

    Level of access:

        |    Conditions   | Public  | Default | Private  | Protected | Friend  | Protected Firend |
        |  -------------- | ------- | ------- | -------- | --------- | ------- | ---------------- |
        |  Class          | - [x]   | - [x]   |  - [x]   |   - [x]   |  - [x]  |      - [x]       |
        |  subclass       | - [x]   | - [x]   |  - [ ]   |   - [ ]   |  - [x]  |      - [ ]       |
        |  Derived Class  | - [x]   | - [x]   |  - [ ]   |   - [x]   |  - [x]  |      - [ ]       |
        |  Globally       | - [x]   | - [ ]   |  - [ ]   |   - [ ]   |  - [ ]  |      - [ ]       |
        |  Same Package   | - [x]   | - [ ]   |  - [ ]   |   - [ ]   |  - [x]  |      - [x]       |
        |  Diff. Package  | - [x]   | - [ ]   |  - [ ]   |   - [ ]   |  - [ ]  |      - [x]       |
        
8. How do we modify protected data?
    By using setter and getters

9. Why setters, getters are kept public but the data is kept private?
    Apart from data encapsulation and easier future modifications here is a list of pros for keeping them public:
        1. Encapsulation of behavior associated with getting or setting the property - this allows additional functionality (like validation) to be added more easily later.
        2. Hiding the internal representation of the property while exposing a property using an alternative representation.
        3. Insulating your public interface from change - allowing the public interface to remain constant while the implementation changes without affecting existing consumers.
        4. Controlling the lifetime and memory management (disposal) semantics of the property - particularly important in non-managed memory environments (like C++ or Objective-C).
        5. Providing a debugging interception point for when a property changes at runtime - debugging when and where a property changed to a particular value can be quite difficult without this in some languages.
        6. Improved interoperability with libraries that are designed to operate against property getter/setters - Mocking, Serialization, and WPF come to mind.
        7. Allowing inheritors to change the semantics of how the property behaves and is exposed by overriding the getter/setter methods.
        8. Allowing the getter/setter to be passed around as lambda expressions rather than values.
        9. Getters and setters can allow different access levels - for example the get may be public, but the set could be protected.

10. What are different types of argument?
    A parameter is a variable used during the declaration of the function or subroutine, and arguments are passed to the function body, and it should match with the parameter defined. There are two types of Arguments.

        1. Call by Value – Value passed will get modified only inside the function, and it returns the same value whatever it is passed into the function.
        2. Call by Reference – Value passed will get modified in both inside and outside the functions and it returns the same or different value.

11. What is an interface?
    In simple words each class can have its own interface and an interface is like a specsheet of attributes which is used to determine whether the instance qualify to be known as an object or not.
    
    or

    An interface is a collection of an abstract method. If the class implements an interface, it thereby inherits all the abstract methods of an interface.

    To create an interface, interface keyword is used.

12. What is exception handling?
    An exception is an event that occurs during the execution of a program. Exceptions can be of any type – Runtime exception, Error exceptions. Those exceptions are adequately handled through exception handling mechanism like try, catch, and throw keywords.

13. What is a friend function?
    A friend function is a friend of a class that is allowed to access to Public, private, or protected data in that same class. If the function is defined outside the class cannot access such information.

    A friend can be declared anywhere in the class declaration, and it cannot be affected by access control keywords like private, public, or protected.

14. What is this pointer?
    THIS pointer refers to the current object of a class. THIS keyword is used as a pointer which differentiates between the current object with the global object. It refers to the current object.

15. What is difference between structure and a class?
    Class: User-defined blueprint from which objects are created. It consists of methods or set of instructions that are to be performed on the objects.

    Structure: A structure is basically a user-defined collection of variables which are of different data types.

16. What is pure virtual function?
    Pure virtual functions or abstract functions are functions that are only declared in the base class. This means that they do not contain any definition in the base class and need to be redefined in the subclass.

17. How is overloading and overriding done?
    Overloading is static Binding, whereas Overriding is dynamic Binding. Overloading is nothing but the same method with different arguments, and it may or may not return the equal value in the same class itself.
    Operator keyword is used for overloading.

    Overriding is the same method names with the same arguments and return types associated with the class and its child class.



18. What is the difference between OOP and SOP?
    
        | Object oriented programming                                           | Structural Programming                                                       |
        | ------------------------------------------------------------------    | -------------------------------------------------------------------------    | 
        |  OPP is  based on objects rather than just functions and procedures   | Provides logical structure to a program where programs are divided functions |
        |  Bottom-up approach                                                   | Top-down approach                                                            |
        |  Provides data hiding                                                 | Does not provide data hiding                                                 |
        |  Can solve problems of any complexity                                 | Can solve moderate problems                                                  |
        |  Code can be reused thereby reducing redundancy                       | Does not support code reusability                                            |

19. What is Data abtraction and its techniques?
    Data abstraction is a very important feature of OOPs that allows displaying only the important information and hiding the implementation details. For example, while riding a bike, you know that if you raise the accelerator, the speed will increase, but you don’t know how it actually happens. This is data abstraction as the implementation details are hidden from the rider.
    Data abstraction can be achieved through:

        Abstract class
            An abstract class is a class that consists of abstract methods. These methods are basically declared but not defined. If these methods are to be used in some subclass, they need to be exclusively defined in the subclass.
        
        Abstract method

20. What is finalize keyword?
    Finalize method helps to perform cleanup operations on the resources which are not currently used. Finalize method is protected, and it is accessible only through this class or by a derived class.
    Finalize as an object method used to free up unmanaged resources and cleanup before Garbage Collection(GC). It performs memory management tasks.

21. What is Garbage Collection (GC)?
    GC is an implementation of automatic memory management. The Garbage collector frees up space occupied by objects that are no longer in existence.

22. What is a final variable?
    A variable whose value does not change. It always refers to the same object by the property of non-transversity.


# Data Structure & Algorithm

## Time Complexities

### Data Structures
            +--------------------+-----------------------------------------------------------------------------------------------+------------------+
            |   Data Structure   |                                        Time Complexity                                        | Space Complexity |
            +--------------------+-----------------------------------------------+-----------------------------------------------+------------------+
            |                    |                    Average                    |                     Worst                     |       Worst      |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+
            |                    |   Access  |   Search  | Insertion |  Deletion |   Access  |   Search  | Insertion |  Deletion |                  |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+
            |        Array       |    Θ(1)   |    Θ(n)   |    Θ(n)   |    Θ(n)   |    O(1)   |    O(n)   |    O(n)   |    O(n)   |       O(n)       |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+
            |        Stack       |    Θ(n)   |    Θ(n)   |    Θ(1)   |    Θ(1)   |    O(n)   |    O(n)   |    O(1)   |    O(1)   |       O(n)       |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+
            |        Queue       |    Θ(n)   |    Θ(n)   |    Θ(1)   |    Θ(1)   |    O(n)   |    O(n)   |    O(1)   |    O(1)   |       O(n)       |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+
            | Singly linked list |    Θ(n)   |    Θ(n)   |    Θ(1)   |    Θ(1)   |    O(n)   |    O(n)   |    O(1)   |    O(1)   |       O(n)       |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+
            | Doubly Linked List |    Θ(n)   |    Θ(n)   |    Θ(1)   |    Θ(1)   |    O(n)   |    O(n)   |    O(1)   |    O(1)   |       O(n)       |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+
            |      Skip List     | Θ(log(n)) | Θ(log(n)) | Θ(log(n)) | Θ(log(n)) |    O(n)   |    O(n)   |    O(n)   |    O(n)   |    O(n log(n))   |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+
            |     Hash Table     |    N/A    |    O(1)   |    O(1)   |    O(1)   |    N/A    |    O(n)   |    O(n)   |    O(n)   |       O(n)       |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+
            | Binary Search Tree | Θ(log(n)) | Θ(log(n)) | Θ(log(n)) | Θ(log(n)) |    O(n)   |    O(n)   |    O(n)   |    O(n)   |       O(n)       |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+
            |   Cartesian Tree   |    N/A    | Θ(log(n)) | Θ(log(n)) | Θ(log(n)) |    N/A    |    O(n)   |    O(n)   |    O(n)   |       O(n)       |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+
            |       B-Tree       | Θ(log(n)) | Θ(log(n)) | Θ(log(n)) | Θ(log(n)) | O(log(n)) | O(log(n)) | O(log(n)) | O(log(n)) |       O(n)       |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+
            |   Read-Black Tree  | Θ(log(n)) | Θ(log(n)) | Θ(log(n)) | Θ(log(n)) | O(log(n)) | O(log(n)) | O(log(n)) | O(log(n)) |       O(n)       |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+
            |     Splay Tree     |    N/A    | Θ(log(n)) | Θ(log(n)) | Θ(log(n)) |    N/A    | O(log(n)) | O(log(n)) | O(log(n)) |       O(n)       |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+
            |      AVL Tree      | Θ(log(n)) | Θ(log(n)) | Θ(log(n)) | Θ(log(n)) | O(log(n)) | O(log(n)) | O(log(n)) | O(log(n)) |       O(n)       |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+
            |       KD Tree      | Θ(log(n)) | Θ(log(n)) | Θ(log(n)) | Θ(log(n)) |    O(n)   |    O(n)   |    O(n)   |    O(n)   |       O(n)       |
            +--------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------------------+

### Sorting Algorithm

            +----------------+-----------------------------------------------+------------------+
            |    Algorithm   |                Time Complexity                | Space Complexity |
            +----------------+-------------+-----------------+---------------+------------------+
            |                |     Best    |     Average     |     Worst     |       Worst      |
            +----------------+-------------+-----------------+---------------+------------------+
            | Quicksort      | Ω(n log(n)) | Θ(n log(n))     | O(n^2)        | O(n log(n))      |
            +----------------+-------------+-----------------+---------------+------------------+
            | Mergesort      | Ω(n log(n)) | Θ(n log(n))     | O(n log(n))   | O(n)             |
            +----------------+-------------+-----------------+---------------+------------------+
            | Timesort       | Ω(n)        | Θ(n log(n))     | O(n log(n))   | O(n)             |
            +----------------+-------------+-----------------+---------------+------------------+
            | Heapsort       | Ω(n log(n)) | Θ(n log(n))     | O(n log(n))   | O(1)             |
            +----------------+-------------+-----------------+---------------+------------------+
            | Bubble sort    | Ω(n)        | Θ(n ^ 2)        | O(n^2)        | O(1)             |
            +----------------+-------------+-----------------+---------------+------------------+
            | Insertion sort | Ω(n)        | Θ(n ^ 2)        | O(n^2)        | O(1)             |
            +----------------+-------------+-----------------+---------------+------------------+
            | Selection Sort | Ω(n ^ 2)    | Θ(n ^ 2)        | O(n^2)        | O(1)             |
            +----------------+-------------+-----------------+---------------+------------------+
            | Tree sort      | Ω(n log(n)) | Θ(n log(n))     | O(n^2)        | O(n)             |
            +----------------+-------------+-----------------+---------------+------------------+
            | Shell sort     | Ω(n log(n)) | Θ(n log(n) ^ 2) | O(n(log(n)^2) | O(1)             |
            +----------------+-------------+-----------------+---------------+------------------+
            | Bucket sort    | Ω (n + k )  | Θ(n + K)        | O(n^2)        | O(n)             |
            +----------------+-------------+-----------------+---------------+------------------+
            | Radix sort     | Ω (nk )     | Θ(n + K)        | O(nk)         | O(n+k)           |
            +----------------+-------------+-----------------+---------------+------------------+
            | Counting sort  | Ω (n + k )  | Θ(n + K)        | O(n+k)        | O(k)             |
            +----------------+-------------+-----------------+---------------+------------------+
            | Cube sort      | Ω (n)       | Θ(n log(n))     | O(n log(n))   | O(n)             |
            +----------------+-------------+-----------------+---------------+------------------+
            |                |             |                 |               |                  |
            +----------------+-------------+-----------------+---------------+------------------+

## Interview Questions

1.  