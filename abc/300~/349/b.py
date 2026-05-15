import sys
s=input()
dic={}
se=set()
for i in range(len(s)):
    if s[i] in se:
        dic[s[i]]+=1
    else:
        dic[s[i]]=1
        se.add(s[i])
for i in range(1,len(s)+1):
    count=0
    for q in dic:
        #print(dic[q],count)
        if dic[q]==i:
            count+=1
    if count==0 or count==2:
        continue
    else:
        print("No")
        sys.exit()

print("Yes")