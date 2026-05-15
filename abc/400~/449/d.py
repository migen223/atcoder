
l,r,d,u=map(int,input().split())

def count(w,h):
    ans=0
    if h==0 or w==0:
        return 0
    if h==1:
        return w//2 
    if w==1:
        return h//2
    
    for i in range(2,h+1,2):
        now=abs(i)
        up=max(w,0)
        #print("now,up",up,now)
        if 0<=now<=up:
            ans+=now
        else:
            ans+=up
    
    #print("ans",ans)
    
    for i in range(2,w+1,2):
        now=abs(i)
        up=max(h,0)
        #print("now,up",now,up)
        if 0<=now<=up:
            ans+=now
        else:
            ans+=up
    #print("ans",ans)
    ans-=min(h,w)//2
    return ans

width=[]
if l*r<0:
    width.append((1,abs(l)))
    width.append((1,r))
else:
    width.append((min(abs(l),abs(r)),max(abs(l),abs(r))))
height=[]
if d*u<0:
    height.append((1,abs(d)))
    height.append((1,u))
else:
    height.append((min(abs(d),abs(u)),max(abs(d),abs(u))))

ans=0
for h in height :
    for w in width:
        ans+=count(w[1],h[1])-count(w[0]-1,h[1])-count(w[1],h[0]-1)+count(w[0]-1,h[0]-1)

for i in range(l,r+1):
    if d*u<0:
        if abs(i)%2==0:
            ans+=1

for i in range(d,u+1):
    if l*r<0:
        if abs(i)%2==0:
            ans+=1

if l*r<0 and d*u<0:
    ans-=1
print(ans)