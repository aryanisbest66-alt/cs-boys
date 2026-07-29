n=int(input("enter the number of row"))
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(65+j),end=' ')
    print()
