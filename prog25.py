##Find Maximum repeated character count in a string

def max_repeated_char_count(s):
   
    char_count = {}
    
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
   
    max_count = max(char_count.values())
    
    
    max_chars = [char for char, count in char_count.items() if count == max_count]
    
   
    print(f"The maximum repeated character count is {max_count} for the character(s): {', '.join(max_chars)}")


max_repeated_char_count("hello world")
max_repeated_char_count("mississippi")
max_repeated_char_count("abcdefghijklmnopqrstuvwxyz")
