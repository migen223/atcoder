from collections import Counter
s=input()

c=Counter(s)
se=set()
mc=c.most_common()
se.add(mc[0][0])
ma=mc[0][1]
for st,n in mc:
    if n!=ma:
        break
    se.add(st)
#print(se,ma)
ans=[]
for i in s:
    if i in se:
        continue
    ans.append(i)
print("".join(ans))