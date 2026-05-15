n=int(input())
genso=[]
for i in range(n):
    a=list(map(int,input().split()))
    genso.append(a)
now=0
for i in range(n):
    now=genso[max(i,now)][min(i,now)]-1
print(now+1)