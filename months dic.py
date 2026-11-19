d= {'jan':31,'feb':28,'mar':31,'apr':30,'may':31 ,'jun':30,'jul':31,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}
data=[]
for i in d:
    data.append([d[i],i])
data.sort()
dnew= {}
for i in data:
    dnew[i[1]]=i[0]
print("dictionary sorted by number of days in month",dnew) 
