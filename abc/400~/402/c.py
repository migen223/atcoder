n,m=map(int,input().split())
foods=[]
guzai=[]
for a in range(n):
    guzai.append([])
for i in range(m):
    j=input()
    l=list(map(int,j.split()))
    del(l[0])
    for k in l:
        guzai[k-1].append(i)
    foods.append(len(l))

i=input()
kokuhuku=list(map(int,i.split()))
cooked=[False]*m
for q in range(len(kokuhuku)):
    kokuhuku[q]-=1

c=0
for i in kokuhuku:
    
    for j in guzai[i]:
        if cooked[j]:
            continue
        foods[j]-=1

        if foods[j]==0:
            c+=1 
            cooked[j]=True 
    print(c)

"""
newfoods=foods.copy()
for k in kokuhuku:
    count=0
    for f in range(len(foods)):
        if k in foods[f]:
             newfoods[f].remove(k)
    for a in newfoods:
        if len(a)==0:
            count+=1
    print(count)
"""
