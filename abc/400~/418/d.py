
n=int(input())
t=input()

ans=0
dpe=[0]*n
dpo=[0]*n

if t[0]=="1":
    dpe[0]=1
else:
    dpo[0]=1

for i in range(1,n):
    if t[i]=="0":
        dpo[i]=dpe[i-1]+1
        dpe[i]=dpo[i-1]
    else:
        dpe[i]=dpe[i-1]+1
        dpo[i]=dpo[i-1]
#print(dpe)
#print(dpo)
print(sum(dpe))





"""
011011100101110111100010011010

01
11
"""

