import sys
n,m,h,k=map(int,input().split())
s=input()

gettable=set()
dic={}
items=[list(map(int,input().split())) for i in range(m)]
for i in range(m):
    gettable.add((items[i][0],items[i][1]))

now=[0,0]
for i in range(n):
    h-=1
    #print(h,now,gettable)
    if s[i]=="R":
        now[0]+=1
    if s[i]=="L":
        now[0]-=1
    if s[i]=="U":
        now[1]+=1
    if s[i]=="D":
        now[1]-=1
    if (now[0],now[1])in gettable and h<k:
        h=k
        gettable.remove((now[0],now[1]))
    if h==0 and i!=n-1:
        print("No")
        sys.exit()
print("Yes")




