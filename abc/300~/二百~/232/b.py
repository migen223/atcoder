import sys
s=list(input())
t=list(input())
dic1={}
dic2={}

for i in range(97, 123):
    dic1[chr(i)]=i-97
    dic2[i-97]=chr(i)

for i in range(27):
    ans=[]
    for j in range(len(s)):
        ans.append(dic2[(dic1[s[j]]+i)%26])
    if ans==t:
        print("Yes")
        sys.exit()

print("No")
