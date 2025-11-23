# Python Interview Questions

## Basic Python

1. What is pep 8?

    Ans: PEP stands for Python Enhancement Proposal. It is a set of rules that specify how to format Python code for maximum readability.

2. How is memory managed in Python?

    Ans: Memory is managed in Python in the following ways:

    1. Memory management in python is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap. The python interpreter takes care of this instead.
    2. The allocation of heap space for Python objects is done by Python’s memory manager. The core API gives access to some tools for the programmer to code.
    3. Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made available to the heap space.

3. What is __init__?

    Ans: __init__ is a method or constructor in Python. This method is automatically called to allocate memory when a new object/ instance of a class is created. All classes have the __init__ method.

    Here is an example of how to use it.

    class Employee:

        def __init__(self, name, age,salary):

        self.name = name

        self.age = age

        self.salary = 20000

        E1 = Employee("XYZ", 23, 20000)

        # E1 is the instance of class Employee.

        #__init__ allocates memory for E1.

        print(E1.name)

        print(E1.age)

        print(E1.salary)

4. What is a lambda function?

    Ans: An anonymous function is known as a lambda function. This function can have any number of parameters but, can have just one statement.

    Example:

        a = lambda x,y : x+y

        print(a(5, 6))

        Output: 11

5. What is self in Python?

    Ans: Self is an instance or an object of a class. In Python, this is explicitly included as the first parameter. However, this is not the case in Java where it’s optional.  It helps to differentiate between the methods and attributes of a class with local variables.

    The self variable in the init method refers to the newly created object while in other methods, it refers to the object whose method was called.

6. How does break, continue and pass work?

    Break:  Allows loop termination when some condition is met and the control is transferred to the next statement.

    Continue:   Allows skipping some part of a loop when some specific condition is met and the control is transferred to the beginning of the loop

    Pass:   Used when you need some block of code syntactically, but you want to skip its execution. This is basically a null operation. Nothing happens when this is executed.

7. What does [::-1] do?

    Ans: [::-1] is used to reverse the order of an array or a sequence.
    For example:

    import array as arr

    My_Array=arr.array('i',[1,2,3,4,5])

    My_Array[::-1]

    Output: array(‘i’, [5, 4, 3, 2, 1])

    [::-1] reprints a reversed copy of ordered data structures such as an array or a list. the original array or list remains unchanged.

8. What is pickling and unpickling?

    Ans: Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling. While the process of retrieving original Python objects from the stored string representation is called unpickling.  

9. What does this mean: *args, **kwargs? And why would we use it?

    Ans: We use *args when we aren’t sure how many arguments are going to be passed to a function, or if we want to pass a stored list or tuple of arguments to a function.**kwargs is used when we don’t know how many keyword arguments will be passed to a function, or it can be used to pass the values of a dictionary as keyword arguments. The identifiers args and kwargs are a convention, you could also use *bob and **billy but that would not be wise.

10. What advantages do NumPy arrays offer over (nested) Python lists?

    Ans:  
    1. Python’s lists are efficient general-purpose containers. They support (fairly) efficient insertion, deletion, appending, and 2. concatenation, and Python’s list comprehensions make them easy to construct and manipulate.
    2. They have certain limitations: they don’t support “vectorized” operations like elementwise addition and multiplication, and the fact that they can contain objects of differing types mean that Python must store type information for every element, and must execute type dispatching code when operating on each element.
    3. NumPy is not just more efficient; it is also more convenient. You get a lot of vector and matrix operations for free, which sometimes allow one to avoid unnecessary work. And they are also efficiently implemented.
    4. NumPy array is faster and You get a lot built in with NumPy, FFTs, convolutions, fast searching, basic statistics, linear algebra, histograms, etc.  

11. What is the difference between deep and shallow copy?

    Ans: Shallow copy is used when a new instance type gets created and it keeps the values that are copied in the new instance. Shallow copy is used to copy the reference pointers just like it copies the values. These references point to the original objects and the changes made in any member of the class will also affect the original copy of it. Shallow copy allows faster execution of the program and it depends on the size of the data that is used.

    Deep copy is used to store the values that are already copied. Deep copy doesn’t copy the reference pointers to the objects. It makes the reference to an object and the new object that is pointed by some other object gets stored. The changes made in the original copy won’t affect any other copy that uses the object. Deep copy makes execution of the program slower due to making certain copies for each object that is been called.  

12. Explain Inheritance in Python with an example.

    Ans: Inheritance allows One class to gain all the members(say attributes and methods) of another class. Inheritance provides code reusability, makes it easier to create and maintain an application. The class from which we are inheriting is called super-class and the class that is inherited is called a derived / child class.

    They are different types of inheritance supported by Python:

    Single Inheritance – where a derived class acquires the members of a single super class.

    Multi-level inheritance – a derived class d1 in inherited from base class base1, and d2 are inherited from base2.

    Hierarchical inheritance – from one base class you can inherit any number of child classes

    Multiple inheritance – a derived class is inherited from more than one base class.  

13. What is Polymorphism in Python?

    Ans: Polymorphism means the ability to take multiple forms. So, for instance, if the parent class has a method named ABC then the child class also can have a method with the same name ABC having its own parameters and variables. Python allows polymorphism.

14. Define encapsulation in Python?

    Ans: Encapsulation means binding the code and the data together. A Python class in an example of encapsulation.

15. How do you do data abstraction in Python?

    Ans: Data Abstraction is providing only the required details and hiding the implementation from the world. It can be achieved in Python by using interfaces and abstract classes.

16. Does python make use of access specifiers?

    Ans: Python does not deprive access to an instance variable or function. Python lays down the concept of prefixing the name of the variable, function or method with a single or double underscore to imitate the behavior of protected and private access specifiers.  

17. What is map function in Python?

    Ans: map function executes the function given as the first argument on all the elements of the iterable given as the second argument. If the function given takes in more than 1 arguments, then many iterables are given. #Follow the link to know more similar functions.  

18. What is scope resolution?

    A scope is a block of code where an object in Python remains relevant. Each and every object of Python functions within its respective scope. Namespaces uniquely identify all the objects inside a program, but these namespaces also have a scope defined for them where you could use their objects without any prefix. It defines the accessibility and the lifetime of a variable.

    Let’s have a look at the scope created at the time of code execution:

    1. A local scope refers to the local objects included in the current function.
    2. A global scope refers to the objects that are available throughout the execution of the code.
    3. A module-level scope refers to the global objects that are associated with the current module in the program.
    4. An outermost scope refers to all the available built-in names callable in the program.
