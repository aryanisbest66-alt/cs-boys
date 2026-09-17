x=int(input("enter the value of x:"))
n=int(input("enter value of n:"))
var= 0
sign= -1
for i in range(1,n+1):
    sign = sign*-1
    var= var+(x**i/2)*sign/i
print("sum of the series is",var)
      
