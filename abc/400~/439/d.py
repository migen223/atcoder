from bisect import bisect_left
n=int(input())
a=list(map(int,input().split()))

three={}
five={}
seven={}

for i in range(n):
    if a[i]%3==0:
        
        if a[i]//3 in three:
            three[a[i]//3].append(i)
        else:
            three[a[i]//3]=[i]
    if a[i]%5==0:
        if a[i]//5 in five:
            five[a[i]//5].append(i)
        else:
            five[a[i]//5]=[i]
    if a[i]%7==0:
        if a[i]//7 in seven:
            seven[a[i]//7].append(i)
        else:
            seven[a[i]//7]=[i]
    
ans=0
for j in five:
    
    if j in three and j in seven:
        for jind in five[j]:
            thmi=bisect_left(three[j],jind)
            semi=bisect_left(seven[j],jind)
            #print(j,jind,thmi,semi)
            ans+=thmi*semi
            ans+=(len(three[j])-thmi)*(len(seven[j])-semi)

"""
print(three)
print(five)
print(seven)
"""
print(ans)