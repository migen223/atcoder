from collections import deque
n=int(input())
s=input()

bra=[]
ket=[]
sec=[]
for i in range(len(s)):
    if s[i]=="(":
        bra.append(i)
    if s[i]==")":
        if len(bra)>0:
            sec.append((bra.pop(),i))
sec.sort(key=lambda x:x[0])
sec=deque(sec)
ans=[]
#print(sec)
if len(sec)>0:

    l,r=sec.popleft()
else:
    l,r=10**6,10**7
for i in range(n):
    
    if l<=i<r:
        continue
    elif i<l:
        ans.append(s[i])
    else:
        if len(sec)>0:

            while sec[0][0]<i:
                sec.popleft()
                if len(sec)==0:
                    l,r=10**6,10**7
                    break
            if len(sec)>0:
                l,r=sec.popleft()
            
        else:
            l,r=10**6,10**7
    #print(l,r,i)
        
print("".join(ans))

