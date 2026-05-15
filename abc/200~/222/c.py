
n,m=map(int,input().split())

people=[[0,i] for i in range(2*n)]

a=[]
for i in range(2*n):
    a.append(input())
#print(a)
for i in range(m):
    for j in range(n):
        p1=people[2*j][1]
        p2=people[2*j+1][1]
       # print(a[p1][i],a[p2][i],p1,p2)
        if a[p1][i]=="G" and a[p2][i]=="C":
            people[2*j][0]-=1
        elif a[p1][i]=="C" and a[p2][i]=="P":
            people[2*j][0]-=1
        elif a[p1][i]=="P" and a[p2][i]=="G":
            people[2*j][0]-=1
        elif a[p2][i]=="G" and a[p1][i]=="C":
            people[2*j+1][0]-=1
        elif a[p2][i]=="C" and a[p1][i]=="P":
            people[2*j+1][0]-=1
            #print(f"p1={p1} {people[p1]},p2={p2} {people[p2]}")
        elif a[p2][i]=="P" and a[p1][i]=="G":
            people[2*j+1][0]-=1
    people.sort()
    #print(people)

for i in range(2*n):
    print(people[i][1]+1)