import sys

n=int(input())
people=[list(map(int,input().split())) for i in range(n)]
s=input()
ys=[]
for i in range(n):
    ys.append(people[i][1])
dic={}
se=set()
for i in range(n):
    if ys[i] not in se:
        se.add(ys[i])
        if s[i]=="R":
            dic[ys[i]]={"R":people[i][0]}
        else:
            dic[ys[i]]={"L":people[i][0]}
    else:
        if s[i]=="R" and "R" in dic[ys[i]]:
            dic[ys[i]]["R"]=min(people[i][0],dic[ys[i]]["R"])
        elif s[i]=="L" and "L" in dic[ys[i]]:
            dic[ys[i]]["L"]=max(people[i][0],dic[ys[i]]["L"])
        elif s[i] not in dic[ys[i]]:
            dic[ys[i]][s[i]]=people[i][0] 
#print(dic)
for i in dic:
    if len(dic[i])>=2:
        if dic[i]["R"]<dic[i]["L"]:
            print("Yes")
            sys.exit()
print("No")



