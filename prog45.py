##Convert arraylist into string

from typing import List


def list_to_string(arr: List) -> str:
   
    str1 = ''.join(str(e) for e in arr)
 
    return str1


arr = ['a', 'b', 'c', 'd']
str1 = list_to_string(arr)
print(str1) 
