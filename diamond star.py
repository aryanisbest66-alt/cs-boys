n=int(input("enter the number of rows"))
for i in range(0,n):
    for j in range(0,n-i):
        print('*',end=' ')
    for j in range(0,2*i):
        print(' ',end=' ')
    for j in range(0,n-i):
       print('*',end=' ')
    print()

for i in range(0,n):
    for j in range(0,i+1):
        print('*',end=' ')
    for j in range(0,2*(n-i)-2):
        print(' ',end=' ')
    for j in range(0,i+1):
        print('*',end=' ')
    print()
