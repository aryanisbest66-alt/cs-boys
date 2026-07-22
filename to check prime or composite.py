a=int(input("enter a number"))
var=0
for i in range(2,(a//2)+1):
    if a%i==0:
       var=1
if var==1:
    print(a,"is composite")
else:
  print(a,"is prime")
       
            
            
        
