##"Write a program to check the vowels in the string.Codoid innovations"

def check_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count


string = "Codoid innovations"
num_vowels = check_vowels(string)


print("Number of vowels in the string:", num_vowels)
