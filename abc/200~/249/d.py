
n=int(input())
a=list(map(int,input().split()))

def comb(c):
    return (c*(c-1))//2

number=[0]*(max(a)+1)
for i in a:
    number[i]+=1

a=sorted(list(set(a)))
ans=0
for i in range(len(a)):
    for j in range(len(a)):
        if a[j]**2>a[i]:
            break
        if a[i]%a[j]==0:
            k=a[i]//a[j]
            if a[j]==k :
                ans+=number[a[i]]*((comb(number[k]))*2+number[k])
            else:
                ans+=number[a[i]]*number[a[j]]*number[k]*2
                #print(i,number[a[i]],number[a[j]],number[k])
    #print(a[i],ans)
print(ans)