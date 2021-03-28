# Classes

Well we all know how to work with classes and how simple it is to define them.
here is a quick example for the sake of discussion

## Class Example

class Person():
    def __init__(self,firsName,lastName):
        self.firstName = firstName
        self.lastName = lastName

## inheritance

let say i want to inherit some properties from the previous class and it is only bound to the attributes then i'm going to use inheritance.

### Class Inheritance Example

class Student(Person):
    def __init__(self,firstName,lastName, id, scores):
        Person.__init__(self,firstName,lastName)
        self.id = id
        self.scores = scores

Here you can see we are using a constructor to inherit all first and last name attributes from the person class and the student itself has independent attributes like id and score.

### Super Function

There can be scenarios where you want to inherit everything properties and methods.
let say there is a child who is obsessed with their father and he/she wants to follow him completely what they'll do is mimic everything which he does i.e. inherit everything from him.

in such cases python has a Super() function which saves us the hassle of writing code.
what it does is it inherits everything from the parent class.

#### Super Function Example

class Matt(Student):
    def __init__(self, firstName,lastName, id, scores, section, class, program):
        Super().__init__(self,fistName,lastName,id,scores)
        self.section = section
        self.class = class
        self.program = program
