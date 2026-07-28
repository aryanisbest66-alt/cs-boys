n=int(input("enyer number of rows"))
for i in range(0,n):
    for j in range(0,n-i-1):
        print('',end='')
    for j in range(0,2*i+1):
        if j==0 or j==2*i:
            print('*',end='')
        else:
            print('',end='')
    print()
