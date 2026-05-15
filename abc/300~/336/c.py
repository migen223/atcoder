from itertools import product
n=int(input())
def ten_to_n(num,n):#numをn進数に変換　返り値はstr
    if num==0:
        return "0"
    else:
        k=0
        while n**k<=num:
            k+=1
        ans=[]
        rang=k
        for i in range(rang):
            k-=1
            keta=num//(n**k)
            num-=keta*(n**k)
            ans.append(str(keta))
        return "".join(ans) 


to5=ten_to_n(n-1,5)
print(int(to5)*2)


"""
ans=[]
for i in range(len(to5)):
    if i==0:
        ans.append(dic0[to5[i]])
    elif i==len(to5)-1:
        ans.append(i)
"""
"""
k-=1
n-=5*(4**k-1)//3
ansl=[]
ran=k+1
for i in range(ran):
    #print(k)
    keta=n//(5**k)
    ansl.append(keta)
    n-=5**k*keta
    k-=1
print(ansl)
ans=[]
dic0={0:2,1:4,2:6,3:8}
dic1={0:8,1:0,2:2,3:4,4:6}
for i in range(len(ansl)):
    if i==0:
        ans.append(str(dic0[ansl[i]]))
    else:
        ans.append(str(dic1[ansl[i]]))
print("".join(ans))
1003314434122120
2006628868244228
1013
2024
13
24
"""
