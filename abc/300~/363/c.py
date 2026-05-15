from itertools import permutations
n,k=map(int,input().split())
s=list(input())
words=set()
ans=0
for i in permutations(s):
    words.add(tuple(i))

for word in words:
    #print(word)
    count=0
    f=0
    includeflag=0
    for i in range(n-k+1):
        f=0
        count=0
        for j in range(k//2):

            #print(word[i+j],word[i+k-1-j])
            if word[i+j]==word[i+k-1-j]:
                count+=1
            else:
                f=1 
                #print("break")
                break
        if count==k//2:
            includeflag=1
            break
    if includeflag==0:
        ans+=1
    #print(ans)
print(ans)