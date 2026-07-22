n=int(input("enter a number"))
count=0
number=n
while  n>0:
    n=n//10
    count=count+1
    ren=0
    n=number
    while n>0:
        r=n%10
        ren=ren+(r**count)
        n=n//10
    if ren==number:
        print(number,"is an armstrong number")
    else:
         print(number,"is not an armstrong number")
         
