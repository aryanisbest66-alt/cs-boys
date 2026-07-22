n=10
f=0
s=1
print(f,s,end='')
for i in range(0,100):
    t=f+s
    print(t,end ='')
    f=s
    s=t
    
