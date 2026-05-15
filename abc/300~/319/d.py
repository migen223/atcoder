
n,m=map(int,input().split())
l=list(map(int,input().split()))

top=10**32
bot=0

def check(leng):
    now=0
    line=1
    for i in range(n):
        if l[i]>leng:
            return 10**6
        if now+l[i]>leng:
            now=l[i]+1
            line+=1
        else:
            now+=l[i]+1
       # print(now,line)
    return line
    
#check(26)     

#"""
while top-bot>1:
    mid=(top+bot)//2
    if check(mid)<=m:
        top=mid
    else:
        bot=mid
print(top)
  #"""  
    
