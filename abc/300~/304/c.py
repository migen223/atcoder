import copy
n,d=map(int,input().split())

people=[]
for i in range(n):
    people.append(list(map(int,input().split())))

virus=set()

able=[[people[0][0],people[0][1],[i for i in range(1,n)],0]]
while able:
    l=[]
    now=able.pop()
    virus.add(now[3])
    app=[]
    #print(now)
    for i in range(len(now[2])):
        if (now[0]-people[now[2][i]][0])*(now[0]-people[now[2][i]][0])+(now[1]-people[now[2][i]][1])*(now[1]-people[now[2][i]][1])<=d*d and now[2][i] not in virus:
            app.append([people[now[2][i]][0],people[now[2][i]][1],[],now[2][i]])
        elif now[2][i] not in virus:
            l.append(now[2][i])
    for i in range(len(app)):
        appl=copy.deepcopy(app[i])
        appl[2]=l
        able.append(appl)
#print(virus)
"""
able=[[people[0][0],people[0][1],0]]
while able:
    now=able.pop()
    virus.add(now[2])
    for i in range(1,n):
        if (now[0]-people[i][0])*(now[0]-people[i][0])+(now[1]-people[i][1])*(now[1]-people[i][1])<=d*d and i not in virus:
            able.append([people[i][0],people[i][1],i])
"""
            
for i in range(n):
    if i in virus:
        print("Yes")
    else:
        print("No")