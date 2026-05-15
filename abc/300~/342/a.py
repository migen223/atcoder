s=input()
dic={}
for i in range(len(s)):
    if s[i]  in dic:
        dic[s[i]]+=1
    else:
        dic[s[i]]=1

for i in dic:
    if dic[i]>=2:
        word=i
for i in range(len(s)):
    if s[i]!=word:
        print(i+1)
        break