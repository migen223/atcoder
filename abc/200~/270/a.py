a,b=map(int,input().split())

s=[0,0,0]
if a==1:
    s[0]+=1
elif a==2:
    s[1]+=1
elif a==3:
    s[0]+=1
    s[1]+=1
elif a==4:
    s[2]+=1
elif a==5:
    s[0]+=1
    s[2]+=1
elif a==6:
    s[1]+=1
    s[2]+=1
elif a==7:
    s[0]+=1
    s[1]+=1
    s[2]+=1

if b==1:
    s[0]+=1
elif b==2:
    s[1]+=1
elif b==3:
    s[0]+=1
    s[1]+=1
elif b==4:
    s[2]+=1
elif b==5:
    s[0]+=1
    s[2]+=1
elif b==6:
    s[1]+=1
    s[2]+=1
elif b==7:
    s[0]+=1
    s[1]+=1
    s[2]+=1

ans=0
if s[0]!=0:
    ans+=1
if s[1]!=0:
    ans+=2
if s[2]!=0:
    ans+=4
print(ans) 