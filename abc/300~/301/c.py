import sys
s=list(input())
t=list(input())
s.sort()
t.sort()

sa=0
ta=0
swords=set()
swordd={}
twords=set()
twordd={}
tw=[]
sw=[]
for i in range(len(s)):
    if s[i]=="@":
        sa+=1
    else:
        sw.append(s[i])
        if s[i] not in swords:
            swords.add(s[i])
            swordd[s[i]]=1
        else:
            swordd[s[i]]+=1
    if t[i]=="@":
        ta+=1
    else:
        tw.append(t[i])
        if t[i] not in twords:
            twords.add(t[i])
            twordd[t[i]]=1
        else:
            twordd[t[i]]+=1
#print(sa,swordd)
#print(ta,twordd)

tneed={}
sneed={}
for i in swordd:
    if i in twords:
        if swordd[i]>twordd[i]:
            tneed[i]=swordd[i]-twordd[i]
    else:
        tneed[i]=swordd[i]

for i in twordd:
    if i in swords:
        if twordd[i]>swordd[i]:
            sneed[i]=twordd[i]-swordd[i]
    else:
        sneed[i]=twordd[i]

words=["a","t","c","o","d","e","r"]

counts=0
for i in sneed:
    if i not in words:
        print("No")
        sys.exit()
    else:
        counts+=sneed[i]
countt=0
for i in tneed:
    if i not in words:
        print("No")
        sys.exit()
    else:
        countt+=tneed[i]
if counts>sa or countt>ta:
    print("No")
else:
    print("Yes")



