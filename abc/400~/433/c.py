
s=input()
n=len(s)

rle=[]
now=s[0]
count=0
for i in range(n):
    if now!=s[i]:
        rle.append((int(now),count))
        now=s[i]
        count=1
    else:
        count+=1
rle.append((int(now),count))
#print(rle)

ans=0
for i in range(len(rle)-1):
    if rle[i][0]+1==rle[i+1][0]:
        ans+=min(rle[i][1],rle[i+1][1])
print(ans)
