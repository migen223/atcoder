import sys
s=input()
dic={}
for  i in range(3):
    if s[i] not in dic:
        dic[s[i]]=1
    else:
        dic[s[i]]+=1
for i in range(3):
    if dic[s[i]]==1:
        print(s[i])
        sys.exit()
print(-1)
