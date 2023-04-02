##Write a program to print all the prime numbers between two numbers

def is_prime(n):

    if n < 2:
        return False
   
    for i in range(2, n):
        if n % i == 0:
            return False
   
    return True


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))


print(f"Prime numbers between {start} and {end}:")
for i in range(start, end+1):
    if is_prime(i):
        print(i)

