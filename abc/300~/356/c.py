from itertools import product
n,m,k=map(int,input().split())
#2**15=3.2*10^4
comb=[]
for c in product([True,False],repeat=n):
    comb.append(list(c))

resultl=[]
cl=[]
al=[]
for i in range(m):
    s=input().split()
    c=int(s[0])
    result=s[-1]
    a=[int(s[i])-1 for i in range(1,c+1)]
    resultl.append(result)
    cl.append(c)
    al.append(a)
ans=0
for i in comb:
    check=0
    #print(i)
    for j in range(m):#j回目のテストケース
        count=0
        for q in range(cl[j]):#k番目の鍵
            if i[al[j][q]]:
                count+=1
        if count>=k and resultl[j]=="o":
            check+=1
        elif count<k and resultl[j]=="x":
            check+=1
        else:
            break
        #print(count,check)
    if check==m:
        ans+=1
        
print(ans)



