data={}
ch= 'y'
while ch== 'y':
    team= input("enter team name")
    wins= int(input("enter number of wins"))
    loss= int(input("enter no of losses"))
    mdata= [wins,loss]
    data[team]= mdata
    ch= input("want to enter more teams data enter y/n")
teamname= input("enter team name")
if teamname in data:
    winpercentage=(data[teamname][0]/sum(data[teamname]))
    print("winning percentage of",teamname,"is",winpercentage)
else:
    print("team does notexist")
