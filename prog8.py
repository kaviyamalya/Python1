
##Python program to determine whether the given number is a Harshad Number

def is_harshad_number(n):
    
    digits = list(str(n))
    
    
    digit_sum = sum([int(d) for d in digits])
    
   
    if n % digit_sum == 0:
        return True
    else:
        return False


number = 20
if is_harshad_number(number):
    print(f"{number} is a Harshad Number")
else:
    print(f"{number} is not a Harshad Number")
