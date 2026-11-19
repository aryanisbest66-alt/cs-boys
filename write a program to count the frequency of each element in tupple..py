T= (1,2,8,3,4,5,3,7,4,2,10)
S= []
for i in T:
    if i not in S:
         print(T.count(i))
    S.append(i)
    
