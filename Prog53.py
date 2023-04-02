##"Write a program to check the string is palindrome or notMadam           wow             cycle"

def is_palindrome(string):
   
    string = string.lower().replace(" ", "")
   
    return string == string[::-1]


strings = ["Madam", "wow", "cycle"]
for string in strings:
    if is_palindrome(string):
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")
