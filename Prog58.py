##"Change the vowel characters to ”S” Python    Pythsn"

def replace_vowels(string):
   
    vowels = ["a", "e", "i", "o", "u"]
    
    for vowel in vowels:
        string = string.replace(vowel, "S")
   
    return string


strings = ["Python"]
for string in strings:
    new_string = replace_vowels(string)
    print(f"{string} => {new_string}")
