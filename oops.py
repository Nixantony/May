# oops-object oriented programming
# python supports oops and everything in python considered as object.
# object
# properties&behaviour

# obj:person
# properties:name,age,height
# behaviour:able to walk,able to talk

# properties mentioned using variables
# name="Amal"
# behaviours mentioned using functions/methods
# def display()

# obj:bike,car,bus
# class:vehicle

# Class
# class is an object constructor,(blueprint of an object)
# class:human

# class person:
# person.p1
# person.p2
# person.p3


# Inheritance
# parent-child relation in between classes.

# class Teacher:
#         name,email,age
#         class Student(Teacher):

# Teacher t1
# Student s1

# Abstraction
# polymorphism



# class
# __init__()- assign values to properties and is always executed when the the class is being initiated.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display(self):
        print("Name of the person is: ",self.name)


p1=Person("Amal",22)
p2=Person("Vivek",22)
print(p2.name)
print(p1.age)
p2.display()