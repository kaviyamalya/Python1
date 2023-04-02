##"Remove the duplicate elements in the array without using builtin function[ 5,4,10,20,4,6,10,39,4,39]"

arr = [5, 4, 10, 20, 4, 6, 10, 39, 4, 39]


unique_arr = []


for elem in arr:
   
    if elem not in unique_arr:
      
        unique_arr.append(elem)


print(unique_arr)
