##Implement a program to handle more than one exception

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result: ", result)
    
    # Generate an IndexError
    my_list = [1, 2, 3]
    print("Element at index 5: ", my_list[5])
    
except ValueError:
    print("Invalid input. Please enter an integer.")
    
except ZeroDivisionError:
    print("Cannot divide by zero.")
    
except IndexError:
    print("Index out of range.")
    
except Exception as e:
    print("An error occurred:", e)
    
finally:
    print("End of program.")
