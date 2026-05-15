n=int(input())
s=input()
ans=0
dic={"A":0,"B":0,"C":0}
for i in range(n):
    if s[i] in dic:
        dic[s[i]]+=1
    count=0
    for j in dic:
        if dic[j]!=0:
            count+=1
    if count==3:
        print(i+1)
        break
    