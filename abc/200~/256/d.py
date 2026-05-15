
n=int(input())
ans=[]

l=[]
r=[]
for i in range(n):
    li,ri=map(int,input().split())
    l.append(li)
    r.append(ri)


number=[0]*(max(r)+1)
for i in range(n):
    number[l[i]]+=1
    number[r[i]]-=1

now=0
for i in range(len(number)):
    if now==0 and number[i]>=1:
        ans.append([i])
        now+=number[i]
        continue
    elif now>0 and now+number[i]==0:
        ans[-1].append(i)
        now+=number[i]
        continue
    else:
        now+=number[i]
for i in range(len(ans)):
    print(*ans[i])

