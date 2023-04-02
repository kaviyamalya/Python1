##Constructor Overloading

class Person:
    def __init__(self, name, age=0, gender='Unknown'):
        self.name = name
        self.age = age
        self.gender = gender
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


p1 = Person("kaviya")
p2 = Person("malya", 25)
p3 = Person("siva", 30, "Male")


p1.display()
p2.display()
p3.display()
