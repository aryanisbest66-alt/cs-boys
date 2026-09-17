n=1221

num= n
count= 0
while n>0:
    n = n//10
    count+1
n = num
palin = 0
while n>0:
    r = n%10
    count = count-1
    palin = palin+(10*count)*r
    n= n//10

if palin == num:
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")
