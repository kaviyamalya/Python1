##Implement method overloading & overiding in python

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

class ScientificCalculator(Calculator):
    def add(self, a, b, c, d):
        return super().add(a, b, c) + d


calculator = Calculator()
scientific_calculator = ScientificCalculator()

print(calculator.add(1))              
print(calculator.add(1, 2))              
print(calculator.add(1, 2, 3))           
print(scientific_calculator.add(1, 2, 3, 4)) 


