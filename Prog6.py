#Program to find duplicate values for ArrayList

lst = [1, 2, 3, 4, 2, 5, 3, 6]


unique_values = set()


duplicate_values = []


for value in lst:

    if value in unique_values:
       
        duplicate_values.append(value)
    else:
       
        unique_values.add(value)


print("Duplicate values:", duplicate_values)
