#-------------------- 1 Start --------------------
# Creating a simple class. Create objects for it and
# access variables.

class SomeClass:
    someInt = 10
    someString = "abc"

object1 = SomeClass()
object2 = SomeClass()

print(object1.someInt)
print(object2.someString)

#-------------------- 1 End ----------------------

#-------------------- 2 Start --------------------
# Create a class with "Constructor" method to create
# class variables and methods.
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        print(f"Hello, {self.name}. You are {self.age} years old!")    

    # The __str__ function overrides the default behaviour
    # when an object is printed directly.
    def __str__(self):
        return f"{self.name} = {self.age}"


person1 = Person("John", 30)
person2 = Person("Thomas", 25)

print(person1.greetings())
print(person2.greetings())
person1.age = 10
print(person1.greetings())

print(person1)  # This utilizes __str__ function

del person2 # This deletes the person2 object. After this line of code, Python wont recognize "person2"

#-------------------- 2 End ----------------------
