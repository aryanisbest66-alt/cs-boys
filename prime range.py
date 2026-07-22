a=int(input("enter a numberrange"))
b=int(input("enter second range"))
for i in range(a,b+1):
    flag=0
    for j in range(2,(i//2)+1):
        if i%j==0:
           flag=1
    if flag==0:
        print(i)
        
