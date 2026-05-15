import sys
from collections import Counter
s=list(input())

left=0
right=0
i=0
while s[i]=="a":
    left+=1
    i+=1
    if i==len(s):
        break
i=len(s)-1
while s[i]=="a":
    right+=1
    i-=1
    if i==-1:
        break

word=[]
for i in range(left,len(s)-right):
    word.append(s[i])

if left>right:
    print("No")
else:
    #print(word)
    mid=len(word)//2
    if len(word)%2==1:
        for i in range(1,mid+1):
            if word[mid-i]!=word[mid+i]:
                print("No")
                sys.exit()
    else:
        for i in range(mid):
            if word[i]!=word[-1-i]:
                print("No")
                sys.exit()
    print("Yes")




"""
dic={}
a=[]

for i in range(len(s)):
    if s[i] in dic:
        dic[i].append(i)
    else:
        dic[i]=[i]
    if s[i]=="a":
        a.append(i)

odd=0
odds=[]
for i in dic:
    if len(dic[i])%2==1:
        odd+=1
        odds.append(i)

if odd>1:
    print("No")
elif odd==1:
    left=dic[odds[0]]-1
    right=dic[odds[0]]+1
    for i in range(len(s)):
        if 0<=left and right<len(s):
            if s[left]!=s[right]:
                print("No")
                sys.exit()
        if left<0 and right<len(s):
            if s[right]!="a":
                print("No")
                sys.exit()
        if left<=0 and right>=len(s):
            print("No")
            sys.exit()
        left-=1
        right+=1
        if right>=len(s) and left<0:
            print("Yes")
            sys.exit()
else:

"""



