
n,m=map(int,input().split())

ans=(m*(m-1))//2+m
secr=[]
dic={}
sec=[]
for _ in range(n):
    l,r=map(int,input().split())
    sec.append([l,r])
    """
    if r in dic:
        dic[r]=min(dic[r],l)
       
    else:
        dic[r]=l
        secr.append(r)
secr.sort()
sec=[]
#print(secr)
for i in range(len(secr)):
    sec.append([dic[secr[i]],secr[i]])"""
sec.sort(key=lambda x:x[1])

now=1
#print(sec)
for nl,nr in sec:
    #print(now,nl)
    if now <=nl:
        #print((nl-now+1)*(m-nr+1))
        ans-=(nl-now+1)*(m-nr+1)
        now=nl+1
print(ans)