

h,w=map(int,input().split())

if h==1 and w==1:
    print(0)
else:
    for i in range(h):
        for j in range(w):
            ans=4
            if h==1:
                ans-=1
            if w==1:
                ans-=1
            
            if i==0 or i==h-1:
                ans-=1
            if j==0 or j==w-1:
                ans-=1
            print(ans,end=" ")
        print()