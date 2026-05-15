
t=int(input())

def shift(list,l,r):
    ans=[]
    for i in range(l+1,r+1):
        ans.append(list[i])
    ans.append(list[l])
    return ans


dic={}
dic2={}
for i in range(97, 123):
    dic[chr(i)]=i-97
    dic2[i-97]=chr(i)

for _ in range(t):
    n=int(input())
    s=list(input())
    nl=[]
    for i in range(n):
        nl.append(dic[s[i]])
    #print(nl)
    left=-1
    right=n-1
    f=0
    for i in range(n-1):
        if nl[i]>nl[i+1]:
            left=i
            f+=1
            break
    if f==0:
        print("".join(s))
    else:
        for i in range(left+2,n):
            #print(i,nl[left],nl[i])
            if nl[left]<nl[i]:
                right=i-1
                break
        ansl=[]
        for i in range(left):
            ansl.append(nl[i])
        for i in shift(nl,left,right):
            ansl.append(i)
        for i in range(right+1,n):
            ansl.append(nl[i])
        ansstr=[dic2[ansl[i]] for i in range(n)]
        #print(nl)
        #print(left,right)
        print("".join(ansstr))



