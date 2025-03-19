class Greeter:
    def __init__(self, who):
        self.who = who
    def greet(self):
        return f'Hello, {self.who}!'

id = input("Please write your name: ")

class Person:
    def name(self):
        name = id
    def age(self):
        age = 28
    def method(self):
        name_greeter = Greeter(id)
        print(name_greeter.greet())

class Student(Person):
    def student_id(self):
        print("You have a Student ID")
    def student(self):
        name_greeter = Greeter("Student " + id)
        print(name_greeter.greet())


character1=Student()
character1.student_id()
