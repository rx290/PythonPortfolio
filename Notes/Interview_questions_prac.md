# Interview Preparations

## OOP

1. What is encapsulation?

    The attribute of an object to hide the data and set access specifiers for it is known as encapsulation.
        Access specifiers are of three types which are as follows:
            1. Public
            2. Protected
            3. Private

2. What is polymorphism?

    The attribute to exist in multiple forms is known as polymorphism. as per object attribute it means having multiple definitions
    of a method.
    Types:
        1. Static (occurs at compile time i.e. method overloading)
        2. Dynamic (occurs at runtime i.e. method overriding)

3. What is method overloading and overriding?

    Method overloading:
        Creating methods of same name but with different arguments.

    Method overriding
        A feature to redefine the base class methods as per the child class need but the signature meaning, argument passed and return type will remain same.

4. What is inheritance?

    The concept where one class can share its structure and behavior to another class is called inheritance.
    there are several types of inheritance which are as follows:
        1. Single inheritance
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

    These are defined in the parent class with virtual keywords and are overridden in the subclass these are used to achieve runtime polymorphism.

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

    In simple words each class can have its own interface and an interface is like a spec-sheet of attributes which is used to determine whether the instance qualify to be known as an object or not.

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

19. What is Data abstraction and its techniques?

    Data abstraction is a very important feature of OOPs that allows displaying only the important information and hiding the implementation details. For example, while riding a bike, you know that if you raise the accelerator, the speed will increase, but you don’t know how it actually happens. This is data abstraction as the implementation details are hidden from the rider.
    Data abstraction can be achieved through:

        Abstract class
            An abstract class is a class that consists of abstract methods. These methods are basically declared but not defined. If these methods are to be used in some subclass, they need to be exclusively defined in the subclass.
        
        Abstract method

20. What is finalize keyword?

    Finalize method helps to perform cleanup operations on the resources which are not currently used. Finalize method is protected, and it is accessible only through this class or by a derived class.
    Finalize as an object method used to free up unmanned resources and cleanup before Garbage Collection(GC). It performs memory management tasks.

21. What is Garbage Collection (GC)?

    GC is an implementation of automatic memory management. The Garbage collector frees up space occupied by objects that are no longer in existence.

22. What is a final variable?

    A variable whose value does not change. It always refers to the same object by the property of non-transversity.

## Data Structure & Algorithm

### Time Complexities

#### Data Structures

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

#### Sorting Algorithm

            +----------------+-----------------------------------------------+------------------+
            |    Algorithm   |                Time Complexity                | Space Complexity |
            +----------------+-------------+-----------------+---------------+------------------+
            |                |     Best    |     Average     |     Worst     |       Worst      |
            +----------------+-------------+-----------------+---------------+------------------+
            | Quicksort      | Ω(n log(n)) | Θ(n log(n))     | O(n^2)        | O(n log(n))      |
            +----------------+-------------+-----------------+---------------+------------------+
            | Merge sort      | Ω(n log(n)) | Θ(n log(n))     | O(n log(n))   | O(n)            |
            +----------------+-------------+-----------------+---------------+------------------+
            | Time sort       | Ω(n)        | Θ(n log(n))     | O(n log(n))   | O(n)            |
            +----------------+-------------+-----------------+---------------+------------------+
            | Heap sort       | Ω(n log(n)) | Θ(n log(n))     | O(n log(n))   | O(1)            |
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

### Interview Questions

1. Difference between file structure and structure storage structure?

    The key difference between both the data structure is the memory area that is being accessed. When dealing with the structure that resides the main memory of the computer system, this is referred to as storage structure. When dealing with an auxiliary structure, we refer to it as file structures.

2. What is LIFO?

    LIFO is a short form of Last In First Out. It refers how data is accessed, stored and retrieved. Using this scheme, data that was stored last should be the one to be extracted first. This also means that in order to gain access to the first data, all the other data that was stored before this first data must first be retrieved and extracted.

3. What is FIFO?

    FIFO stands for First-in, First-out, and is used to represent how data is accessed in a queue. Data has been inserted into the queue list the longest is the one that is removed first.

4. What are common types of Data Structures?

    1. Array
    2. Queue
    3. Linked list
    4. Heap
    5. Tree
    6. Stack
    7. graph

5. What is a stack?

    A stack is a data structure in which only the top element can be accessed. As data is stored in the stack, each data is pushed downward, leaving the most recently added data on top.

6. What is a queue?

    A queue is a data structure that can simulate a list or stream of data. In this structure, new elements are inserted at one end, and existing elements are removed from the other end.

7. What is a binary tree?

    A binary search tree stores data in such a way that they can be retrieved very efficiently. The left subtree contains nodes whose keys are less than the node’s key value, while the right subtree contains nodes whose keys are greater than or equal to the node’s key value. Moreover, both subtrees are also binary search trees.

8. What data types are applied using recursion?

    Recursion, is a function that calls itself based on a terminating condition, makes use of the stack. Using LIFO, a call to a recursive function saves the return address so that it knows how to return to the calling function after the call terminates.

9. what are multidimensional arrays?

    Multidimensional arrays make use of multiple indexes to store data. It is useful when storing data that cannot be represented using single dimensional indexing, such as data representation in a board game, tables with data stored in more than one column.

10. linked list are linear or non linear in nature? Explain

    It depends on where you intend to apply linked lists. If you based it on storage, a linked list is considered non-linear. On the other hand, if you based it on access strategies, then a linked list is considered linear.

11. what is a heap?

    A Heap is a special Tree-based data structure in which the tree is a complete binary tree. Generally, Heaps can be of two types:

    Max-Heap: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.

    Min-Heap: In a Min-Heap the key present at the root node must be minimum among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.

12. what is an ordered list?

    An ordered list is a list in which each node’s position in the list is determined by the value of its key component, so that the key values form an increasing sequence, as the list is traversed.

13. What is a liner search?

    A linear search refers to the way a target key is being searched in a sequential data structure. In this method, each element in the list is checked and compared against the target key. The process is repeated until found or if the end of the file has been reached.

14. Difference between BFS and DFS?

    <table class="tg">
    <thead>
    <tr>
        <th class="tg-0pky">Sr.No</th>
        <th class="tg-0pky">BFS</th>
        <th class="tg-0pky">DFS</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td class="tg-0pky">1</td>
        <td class="tg-0pky">BFS stands for Breadth First Search.</td>
        <td class="tg-0pky">DFS stands for Depth First Search.</td>
    </tr>
    <tr>
        <td class="tg-0pky">2</td>
        <td class="tg-0pky">BFS(Breadth First Search) uses Queue data structure <br>for finding the shortest path.</td>
        <td class="tg-0pky">DFS(Depth First Search) uses Stack data structure.</td>
    </tr>
    <tr>
        <td class="tg-0pky">3</td>
        <td class="tg-0pky">BFS can be used to find single source shortest path<br>in an unweighted graph, because in BFS, we reach a <br>vertex with minimum number of edges from a source vertex.</td>
        <td class="tg-0pky">In DFS, we might traverse through more edges to <br>reach a destination vertex from a source.</td>
    </tr>
    <tr>
        <td class="tg-0pky">4</td>
        <td class="tg-0pky">BFS is more suitable for searching vertices which are <br>closer to the given source.</td>
        <td class="tg-0pky">DFS is more suitable when there are solutions away from source.</td>
    </tr>
    <tr>
        <td class="tg-0pky">5</td>
        <td class="tg-0pky">BFS considers all neighbors first and therefore not <br>suitable for decision making trees used in games or <br>puzzles.</td>
        <td class="tg-0pky">DFS is more suitable for game or puzzle problems. We make a <br>decision, then explore all paths through this decision. <br>And if this decision leads to win situation, we stop.</td>
    </tr>
    <tr>
        <td class="tg-0pky">6</td>
        <td class="tg-0pky">The Time complexity of BFS is O(V + E) when Adjacency <br>List is used and O(V^2) when Adjacency Matrix is used, <br>where V stands for vertices and E stands for edges.</td>
        <td class="tg-0pky">The Time complexity of DFS is also O(V + E) when Adjacency <br>List is used and O(V^2) when Adjacency Matrix is used, <br>where V stands for vertices and E stands for edges.</td>
    </tr>
    </tbody>
    </table>

15. Heap vs stack?

    The heap is more flexible than the stack. That’s because memory space for the heap can be dynamically allocated and de-allocated as needed. However, the memory of the heap can at times be slower when compared to that stack.

    <table>
    <thead>
    <tr>
        <th>Parameter</th>
        <th>Stack</th>
        <th>Heap</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Type of data structures</td>
        <td>A stack is a linear data structure.</td>
        <td>Heap is a hierarchical data structure.</td>
    </tr>
    <tr>
        <td>Access speed</td>
        <td>High-speed access</td>
        <td>Slower compared to stack</td>
    </tr>
    <tr>
        <td>Space management</td>
        <td>Space managed efficiently by OS so memory will never <br>become fragmented.</td>
        <td>Heap Space not used as efficiently. <br>Memory can become fragmented as blocks of memory <br>first allocated and then freed.<br></td>
    </tr>
    <tr>
        <td>Access</td>
        <td>Local variables only</td>
        <td>It allows you to access variables globally.</td>
    </tr>
    <tr>
        <td>Limit of space size</td>
        <td>Limit on stack size dependent on OS.</td>
        <td>Does not have a specific limit on memory size.</td>
    </tr>
    <tr>
        <td>Resize</td>
        <td>Variables cannot be resized</td>
        <td>Variables can be resized.</td>
    </tr>
    <tr>
        <td>Memory Allocation</td>
        <td>Memory is allocated in a contiguous block.</td>
        <td>Memory is allocated in any random order.</td>
    </tr>
    <tr>
        <td>Allocation and Deallocation</td>
        <td>Automatically done by compiler instructions.</td>
        <td>It is manually done by the programmer.</td>
    </tr>
    <tr>
        <td>Deallocation</td>
        <td>Does not require to de-allocate variables.</td>
        <td>Explicit de-allocation is needed.</td>
    </tr>
    <tr>
        <td>Cost</td>
        <td>Less</td>
        <td>More</td>
    </tr>
    <tr>
        <td>Implementation</td>
        <td>A stack can be implemented in 3 ways simple array based, <br>using dynamic memory, and Linked list based.</td>
        <td>Heap can be implemented using array and trees.</td>
    </tr>
    <tr>
        <td>Main Issue</td>
        <td>Shortage of memory</td>
        <td>Memory fragmentation</td>
    </tr>
    <tr>
        <td>Locality of reference</td>
        <td>Automatic compile time instructions.</td>
        <td>Adequate</td>
    </tr>
    <tr>
        <td>Flexibility</td>
        <td>Fixed size</td>
        <td>Resizing is possible</td>
    </tr>
    <tr>
        <td>Access time</td>
        <td>Faster</td>
        <td>Slower</td>
    </tr>
    </tbody>
    </table>

16. How does bubble sort, selection sort and merge sort work ?

    Selection Sort

        Time Complexity: Θ(n²)
        
        Selection Sort operates in a very simple way; it goes through all the elements in a data-set one by one comparing the value of one element to the next checking to see if the element is smaller, it then saves the smallest element found in a variable and when the iteration is complete, it will insert that saved element to its respective position in that data-set swapping positions with the value in that position.
        This algorithm has an Θ(n²) because in the worst and best-case-scenario we have to iterate through all the n elements in the array and repeat this process n number of times, even if the data-set is already sorted there is no telling if it is until all the iterations in the algorithm are complete.

    Bubble Sort

        Time Complexity: O(n²) — Ω(n)

        I would say that Bubble Sort might be the simplest sorting algorithm. The way this algorithm processes the input is just like a bubble trying to reach out to the surface, within each iteration the algorithm will find the highest value and put it at the end of the data-set or were that value belongs by comparing each pair of elements in the data-set. So Selection Sort sorts from the smallest element to the highest and Bubble Sort from highest to lowest. Bubble sort also sorts the lowest elements to be closer to the left because within each iteration the higher value will swap places with the lower value, so it moves lower elements to the left and higher elements to the right.
        The worst-case scenario for this algorithm would be if all the elements in the data-set were in reverse order making the algorithm make more “swaps”, but we do see that the best-case scenario is not as bad as Selection Sort because unlike Selection Sort this algorithm is smart enough to realize in its first iteration that the data-set is already sorted.
        
        we can see how Bubble Compares each pair in the data-set and swaps the position of the value if the value is larger, pushing the largest values to the right and smallest to the left, building the output from right to left.

        Merge Sort
        
        Time Complexity: Θ(n log n)
        
        Merge Sort is considered to be one of the fastest sorting algorithms, it is a bit more complex than Selection and Bubble Sort but its more efficient. The idea of Merge Sort is to divide the data-set into smaller data-sets, sort those smaller data-sets and then join them (merge them) together. The way this algorithm behaves is by sorting the left side of the data- set first then the right part and them merging them. Merge sort will divide in two the data-set until all the elements are separate then it will start joining from left to right in pairs then those pairs will merge from left to right until there are only two bigger pairs to join. If we think about it, this makes it easy to merge because if we have to parts of a data-set that are both sorted we can then compare the first element in one data-set with the other and determine which one is smaller, therefore, pushing that smaller element first into a new data-set.

        This algorithm has the same Time Complexity for both worst and best-case scenarios because even if the array is sorted(best-case) the algorithm will still have to do the full procedure to determine whether the data-set is sorted or not.

        Quicksort
            
            Time Complexity: Ω(n log(n)) — O(n²)
            
            Quicksort is also one of the fastest algorithms. To perform a Quicksort we need to pick one element in the data-set and use it as something called a “pivot”, a pivot is an element that is used to compare other elements in the data-set and determine in what position they should be. The first pivot can be a random element in the data-set but by convention, the first or last element is used. The first objective will be getting the first pivot to its correct position in the data-set, to achieve this, we have to sort the elements such that all the elements that are bigger than the pivot are sent to the right of the pivot and all the elements that are smaller than the pivot are sent to the left of the pivot.
            To understand this better let’s put an example, say you need to sort a certain number of coffee mugs by size, the way Quicksort would do it is getting the last cup as a pivot and start doing two comparisons we will call the first comparison A and the second comparison B. Comparison A would then start by checking to see if the first cup is larger than the pivot mug if it is, then comparison B will check if the last mug is smaller than the pivot mug if it is then the first element will swap places and comparison A will move to the right one more space and comparison B will move to the left one space. This procedure will continue until comparison A and B cross each other when this happens we know that comparison A’s last position will now be swapped with the pivot mug so that the pivot mug is in its correct and final position because all of the elements to the left of it are smaller and all the elements in the right are bigger.
            To sort the rest of the mugs the algorithm would do the same procedure for the left and right side. First, it would get a new pivot for the left side comparing it to the other elements on the left side and sorting them accordingly and the same procedure would be repeated with the right side until all the mugs are sorted.
            The worst-case scenario of this algorithm would be if the initial pivot picked is extremely small or large. The best-case scenario would that the initial pivot would fit right or somewhere in the middle of the data-set.

17. How does signed and unsigned numbers affect memory?

    In the case of signed numbers, the first bit is used to indicate whether positive or negative, which leaves you with one bit short. With unsigned numbers, you have all bits available for that number. The effect is best seen in the number range (an unsigned 8-bit number has a range 0-255, while the 8-bit signed number has a range -128 to +127.

18. What is the relationship between queue and linked list?

    The structure of queue is based on singly linked list which is dynamic in nature.

19. Give a basic algorithm for searching a binary search tree.

    1. if the tree is empty, then the target is not in the tree, end search
    2. if the tree is not empty, the target is in the tree
    3. check if the target is in the root item
    4. if a target is not in the root item, check if a target is smaller than the root’s value
    5. if a target is smaller than the root’s value, search the left subtree
    6. else, search the right subtree

20. what is a graph?

    A graph is one type of data structure that contains a set of ordered pairs. These ordered pairs are also referred to as edges or arcs and are used to connect nodes where data can be stored and retrieved.

21. linear vs non linear data structures?

    The linear data structure is a structure wherein data elements are adjacent to each other. Examples of linear data structure include arrays, linked lists, stacks, and queues. On the other hand, a non-linear data structure is a structure wherein each data element can connect to more than two adjacent data elements. Examples of nonlinear data structure include trees and graphs.

22. what is an avl tree?

    An AVL tree is a type of binary search tree that is always in a state of partially balanced. The balance is measured as a difference between the heights of the subtrees from the root. This self-balancing tree was known to be the first data structure to be designed as such.

23. what is a doubly linked list?

    Doubly linked lists are a special type of linked list wherein traversal across the data elements can be done in both directions. This is made possible by having two links in every node, one that links to the next node and another one that connects to the previous node

24. What is huffman algorithm?

    Huffman’s algorithm is used for creating extended binary trees that have minimum weighted path lengths from the given weights. It makes use of a table that contains the frequency of occurrence for each data element.

25. what is fibonacci search?

    Fibonacci search is a search algorithm that applies to a sorted array. It makes use of a divide-and-conquer approach that can significantly reduce the time needed in order to reach the target element.

26. Explain recursion?

    Recursive algorithm targets a problem by dividing it into smaller, manageable sub-problems. The output of one recursion after processing one sub-problem becomes the input to the next recursive process.

27. What is hashing?

    Hashing is a technique or process of mapping keys, values into the hash table by using a hash function. It is done for faster access to elements. The efficiency of mapping depends on the efficiency of the hash function used.

    Let a hash function H(x) maps the value x at the index x%10 in an Array. For example if the list of values is [11,12,13,14,15] it will be stored at positions {1,2,3,4,5} in the array or Hash table respectively.

28. What is a spanning tress?

    A spanning tree is a subset of Graph G, which has all the vertices covered with minimum possible number of edges. A spanning tree does not have cycles and it can not be disconnected.

29. What are greedy algorithm?

    The below given problems find their solution using greedy algorithm approach −

        Travelling Salesman Problem
        Prim's Minimal Spanning Tree Algorithm
        Kruskal's Minimal Spanning Tree Algorithm
        Dijkstra's Minimal Spanning Tree Algorithm
        Graph - Map Coloring
        Graph - Vertex Cover
        Knapsack Problem
        Job Scheduling Problem

30. what is an algorithm?

    Algorithm is a step by step procedure, which defines a set of instructions to be executed in certain order to get the desired output.

31. which DS should be used for implementing LRU cache?

    We use two data structures to implement an LRU Cache.

    Queue which is implemented using a doubly linked list. The maximum size of the queue will be equal to the total number of frames available (cache size). The most recently used pages will be near rear end and least recently pages will be near front end.

    A Hash with page number as key and address of the corresponding queue node as value. See How to implement LRU caching scheme? What data structures should be used?

## Database Interview Questions

### Most common Interview Questions

1. What is RDBMS?

   That type of database which uses tables to store data. which are also used to create relationship with other stored dataset are known as Relation Database Management system.

2. What are records?

   A collection of sequential fields with different data types to store data in a table is known as a record.

3. What are advantages of RDBMS?

    1. Simplicity in Data Models
    2. Data Accuracy
    3. Data is easy to access
    4. Data integrity
    5. Flexibility
    6. Normalization
    7. it welcomes future proofing i.e. it welcomes future modifications
    8. High Security

4. What is Data Redundancy?

   Occurrence or storing of same data at different locations are known as data redundancy.

5. What are Database Relationships?

   1. 1 - 1
   2. 1 - many
   3. many - 1
  
6. Explain Normalization and De-normalization?

   Normalization:
    1. Normalization is used to remove redundant data from DB and to store non redundant and consistent data into it.
    2. It uses optimized memory hence faster in performance.
    3. Normalization is generally used where no. of CURD operations are performed and joins of the tables are not expensive.

    De-normalization:
    1. It is used to combine multiple table into a single table so that it could be queried quickly.
    2. it introduces redundancy for faster execution of queries.
    3. Joins are expensive and the queries are frequently executed on the tables.

7. Why is indexing used?

   Indexes are used to quickly locate data without having to search every row in the database table every time a database table is accessed.
   Indexes can be created using or or more fields of Tables which provides basis of both rapid random lookups and efficient access of ordered records.

8. Types of SQL Statements? and State DDL , DML and DCL Clauses?

   1. DDL: Data Definition Language
   2. DML: Data Manipulation language
   3. DCL: Data Control Language
   4. DDL
       1. Create
       2. Alter
       3. Truncate
       4. Drop
       5. Rename
   5. DML
      1. Insert
      2. Update
      3. Delete
      4. Merge
   6. DCL
      1. Commit
      2. Rollback
      3. Save point

9. Difference between Having and Where Clause?

    Where Clause:
        Where clause is used for filtration purposes i.e. while joining one or more table or fetching only specific records which are going to satisfy a specific condition for e.g:

        select * from Student where age >= 21;

    Having Clause:
        Having clause is used when aggregated functions or calculations are going to get performed in the queries. for e.g:

        select Item, sum(Amount) as Net_amount from Transaction group by item having sum(Net_amount) > 1200;

10. What are views?

    A virtual tables based on the result set of a query performed on one or more real tables.

11. What are cursors and its type?

    Cursors are temporary work area created in the main memory of a system when sql queries are executed. These work areas contain information on a select statement and the rows of data accessed by the query.
    This work area is used to store, retrieve and manipulate data from the database.
    There are two types of cursors which are as follows:
        1. implicit Cursors (Created by default)
        2. Explicit Cursors (must be created)

12. What are database transactions?

    A single module / unit / logic or procedure which is made up of multiple operations is known as a transaction. for example:
    a bank transfer requires checking of the balance whether they have sufficient funds or not then subtracting the amount from their bank account and transferring it to the targeted account by adding transferred amount to their current balance.  

13. What are database lock?

    A mechanism to ensure data consistency. it occurs when a transaction starts and it ends when the transaction is completed in order to prevent further changes from other sources for that particular transaction.

14. Define Joins and explain its types?

    There are several types of joins which are as follows:
    1. Left Join : Returns all records from the left table, and the matched records from the right table
    2. Right Join : Returns all records from the right table, and the matched records from the left table
    3. Inner Join : Returns records that have matching values in both tables
    4. Full Outer Join : Returns all records when there is a match in either left or right table
    5. Cross Join :  it returns a cartesian product of the tables if where clause is not used otherwise it returns same results as an inner join
    6. Self Join

15. What are aggregated functions?

    An aggregate function performs a calculation on a set of values, and returns a single value. Except for COUNT(*) , aggregate functions ignore null values. Aggregate functions are often used with the GROUP BY clause of the SELECT statement. All aggregate functions are deterministic.
    list of aggregated functions:
        1. AVG
        2. Count
        3. Max
        4. Min
        5. Sum

16. What are keys?

    KEYS in DBMS is an attribute or set of attributes which helps you to identify a row(tuple) in a relation(table). They allow you to find the relation between two tables. Key is also helpful for finding unique record or row from the table.
    Types of keys:
    1. Super Key -  A super key is a group of single or multiple keys which identifies rows in a table.
    2. Primary Key -  is a column or group of columns in a table that uniquely identify every row in that table.
    3. Candidate Key -  is a set of attributes that uniquely identify tuples in a table. Candidate Key is a super key with no repeated attributes.
    4. Alternate Key -  is a column or group of columns in a table that uniquely identify every row in that table.
    5. Foreign Key -  is a column that creates a relationship between two tables. The purpose of Foreign keys is to maintain data integrity and allow navigation between two different instances of an entity.
    6. Compound Key -  has two or more attributes that allow you to uniquely recognize a specific record. It is possible that each column may not be unique by itself within the database.
    7. Composite Key -  An artificial key which aims to uniquely identify each record is called a surrogate key. These kind of key are unique because they are created when you don't have any natural primary key.
    8. Surrogate Key -  An artificial key which aims to uniquely identify each record is called a surrogate key. These kind of key are unique because they are created when you don't have any natural primary key. 

17. Difference between delete and truncate and drop?

    | Sr. No. |          Key         |                      Delete                     |                      Truncate                      |
    |:-------:|:--------------------:|:-----------------------------------------------:|:--------------------------------------------------:|
    | 1       | Basic                | It is used to delete specific data              | It is used to delete the entire data of the table  |
    | 2       |        Where clause  | We can use with where clause                    | It can’t be used with where clause                 |
    | 3       | Locking              | It locks the table row before deleting the row  | It locks the entire table                          |
    | 4       | Rollback             | We can rollback the changes.                    | We can’t rollback the changes                      |
    | 5       | Performance          | It is slower than truncate                      | It is faster than delete                           |

18. What is normalization and its types?

    Database Normalization is a process and it should be carried out for every database you design. The process of taking a database design, and apply a set of formal criteria and rules, is called Normal Forms.

    The database normalization process is further categorized into the following types:

    1. First Normal Form (1 NF): records should have atomic values
    2. Second Normal Form (2 NF): 1NF, every non key field must depend on primary key, no partial dependencies
    3. Third Normal Form (3 NF): 2nf, no transitive functional dependency
    4. Boyce Codd Normal Form or Fourth Normal Form ( BCNF or 4 NF): not having more than one candidate key
    5. Fifth Normal Form (5 NF): can't be divided into smaller tables without loss of data
    6. Sixth Normal Form (6 NF): isn't standardized yet

19. Find Second Highest Salary?

    Select Max(salary) from employee order by salary DESC n-1, 1;
