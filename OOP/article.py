class Person:
    def greet(self):
        print("Hello, I'm a person!")

class Student(Person):
    def greet(self):
        print("Hello, I'm a student!")

Mary = Person()
Joe = Student()

Mary.greet() 
Joe.greet()