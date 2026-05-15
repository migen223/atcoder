n=int(input())
a=list(map(int,input().split()))
ans=2*n-1
diff=[]

for i in range(n-1):
    diff.append(a[i]-a[i+1])
#print(diff)
count=0
for i in range(n-2):
    #print(count)
    #print(diff[i],diff[i+1])
    if diff[i]==diff[i+1]:
        count+=1
    elif count>=1 and diff[i]!=diff[i+1]:
        ans+=count*(count+1)//2
        count=0
    
ans+=count*(count+1)//2
print(ans)