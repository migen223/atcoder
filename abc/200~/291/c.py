import sys

n=int(input())
s=input()
now=[0,0]
se=set()
se.add((now[0],now[1]))
for i in range(n):
    if s[i]=="R":
        now[0]+=1
    if s[i]=="L":
        now[0]-=1
    if s[i]=="U":
        now[1]+=1
    if s[i]=="D":
        now[1]-=1
    if (now[0],now[1]) in se :
        print("Yes")
        sys.exit()
    else:
        se.add((now[0],now[1]))
    #print(se)
print("No")



