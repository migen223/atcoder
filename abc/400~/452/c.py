
n=int(input())

bone=[]
for _ in range(n):
    a,b=map(int,input().split())
    bone.append((a,b-1))

m=int(input())
word=[]
ma=0
for i in range(m):
    s=input()
    word.append(s)
    ma=max(ma,len(s))

#print(word)
snum={}
for s in word:
    #print(s)
    if len(s) not in snum:
        snum[len(s)]=[set() for _ in range(len(s))]
    for i in range(len(s)):
        snum[len(s)][i].add(s[i])
#print(snum)

for s in word:
    if len(s)==n:
        f=0
        #print(s)
        for i in range(n):
            a,b=bone[i]
            if a in snum:
                #print(snum[a])
                if s[i] not in snum[a][b]:
                    #print(s[i],snum[a][b])
                    f+=1
            else:
                f+=1
        if f==0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
