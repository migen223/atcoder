n,q=map(int,input().split())
ans=0
l=0
r=1
handle=[i for i in range(n)]

for i in range(q):
    h,t=input().split()
    t=int(t)-1
    if h=="L":
        left=l
        for i in range(1,n):
            left=(left-1)%n
            if left==r:
                break
            elif left==t:
                ans+=i
                l=left
               # print(ans)
                break
            
        right=l
        for i in range(1,n):
            right=(right+1)%n
            if right==r:
                break 
            elif right==t:
                ans+=i
                #print(ans)
                l=right
                break
            
       #print(f"l={l}")
    else:
        
        left=r
        #print(r)
        for i in range(1,n):
            left=(left-1)%n
            #print(left)
            if left==l:
                break
            elif left==t:
                ans+=i
                r=left
                #print(ans)
                break

            
        right=r
        #print(right)
        for i in range(1,n):
            right=(right+1)%n
            #print(right,i)
            if right==l:
                break
            elif right==t:
                ans+=i
                #print(ans)
                r=right
                break

        #print(f"r={r}")
            
print(ans)



