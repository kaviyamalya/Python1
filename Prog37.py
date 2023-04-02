##Implement a program for encapsulation

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

person1 = Person("kavia", 25)
person2 = Person("malya", 30)

print(person1.get_name()) 
person1.set_name("siva")
print(person1.get_name()) 

print(person2.get_age()) 
person2.set_age(35)
print(person2.get_age()) 
