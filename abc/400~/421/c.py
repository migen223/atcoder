n=int(input())
s=input()
ab=[0]*(2*n)#-1 ->本来AなのにB
ba=[0]*(2*n)#1 ->本来BなのにA
for i in range(2*n):
    if i%2==0:
        if s[i]=="A":
            ba[i]=-1
        else:
            ab[i]=-1
    else:
        if s[i]=="B":
            ba[i]=1
        else:
            ab[i]=1

count=0
plus=0
nowAorB=0
for i in range(2*n):
    if nowAorB==0:
        if ab[i]==1:
            nowAorB=1
            plus+=1
            continue
        elif ab[i]==-1:
            nowAorB=-1
            plus+=1
            continue
    else:
        if ab[i]==0:
            count+=plus
        elif nowAorB==1 and ab[i]==1:
            count+=plus
            plus+=1
        elif nowAorB==1 and ab[i]==-1:
            count+=plus
            plus-=1
            if plus==0:
                nowAorB=0
        elif nowAorB==-1 and ab[i]==-1:
            count+=plus
            plus+=1
        elif nowAorB==-1 and ab[i]==1:
            count+=plus
            plus-=1
            if plus==0:
                nowAorB=0
ans=count
count=0
plus=0
nowAorB=0
for i in range(2*n):
    if nowAorB==0:
        if ba[i]==1:
            nowAorB=1
            plus+=1
            continue
        elif ba[i]==-1:
            nowAorB=-1
            plus+=1
            continue
    else:
        if ba[i]==0:
            count+=plus
        elif nowAorB==1 and ba[i]==1:
            count+=plus
            plus+=1
        elif nowAorB==1 and ba[i]==-1:
            count+=plus
            plus-=1
            if plus==0:
                nowAorB=0
        elif nowAorB==-1 and ba[i]==-1:
            count+=plus
            plus+=1
        elif nowAorB==-1 and ba[i]==1:
            count+=plus
            plus-=1
            if plus==0:
                nowAorB=0
if ans>count:
    ans=count

print(ans)
"""
AAABABABBBABABBABABABABBAAABABABBA
ABABABABABABABABABABABABABABABABAB
 A      B     BABABABAB  A      BA
"""

