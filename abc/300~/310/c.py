n=int(input())

ans=0
se=set()
for i in range(n):
    s=list(input())

    if tuple(s) in se:
        continue
    else:
        se.add(tuple(s))
        rev=reversed(s)
        se.add(tuple(rev))
        ans+=1
print(ans)

"""
def check(l1,l2):
    count=0
    if l1==l2:
        return True
    else:
        for i in range(len(l1)):
            if l1[i]==l2[-1-i]:
                count+=1
        return count==len(l1)
se=set()
dic={}
for  i in range(n):
    s=list(input())
    ss=sorted(s)
    if tuple(ss) not in se:
        se.add(tuple(ss))
        dic[tuple(ss)]=[s]
    else:
        dic[tuple(ss)].append(s)
#print(dic)
ans=0

for i in dic:
    if len(dic[i])==1:
        ans+=1
    else:
        minus=0
        for j in range(len(dic[i])-1):
            for k in range(j,len(dic[i])):
                if check(dic[i][j],dic[i][k]):
                    minus+=1
        ans+=max((len(dic[i])*len(dic[i]))//2-minus,1)

    #print(ans)


print(ans)

"""