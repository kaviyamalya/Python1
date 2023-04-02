for i in range(1, 101):
   
    for j in range(1, i):
        if j*(j+1) == i:
            print(i, end=' ')
            break
