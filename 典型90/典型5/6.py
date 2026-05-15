from sortedcontainers import SortedList
n,k=map(int,input().split())
s=input()

"""
dic={}
for i in range(97, 123):
    dic[chr(i)]=i-97
l=[dic[s[i]] for i in range(n)]
print(l)
"""

def pop(sl,n,start):
    #print("f",sl,start,s[start],n)
    while s[start]!=n:  
        #print("d",sl,start,s[start],n)      
        sl.remove(s[start])
        start+=1
    sl.remove(s[start])

    return start+1

ans=[]
sl=SortedList([])
for i in range(n-k+1):
    sl.add(s[i])

ans.append(sl[0])
now=sl[0]
start=0
for i in range(k-1):
    start=pop(sl,ans[-1],start)
    sl.add(s[n-k+1+i])
    now=sl[0]
    ans.append(now)
print("".join(ans))