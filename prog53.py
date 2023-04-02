##"5. Write a program to print pattern?


n = int(input("Enter a number: "))


for i in range(n, 0, -1):
   
    print("*" * i, end="")
    
    
    if i != n:
        print(" " * (n - i), end="")
    
   
    print("*" * i)
