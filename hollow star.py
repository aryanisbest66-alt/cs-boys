n=int(input("enter the number of rows"))
for i in range(0,n):
    for j in range(0,n-i):
        print('*',end=' ')
    for j in range(0,2*i):
        print(' ',end=' ')
    for j in range(0,n-i):
       print('*',end=' ')
    print()
