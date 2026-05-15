import sys
n,k=map(int,input().split())
a=list(map(int,input().split()))
se=set(a)
sel=list(se)
sel.sort()
ans=0
#print(sel)
if sel[0]==0:
    i=0
    while i<k-1 and i+1<len(sel):
        if sel[i+1]-sel[i]!=1:
            print(ans+1)
            sys.exit()
        else:
            ans+=1
        #print(ans)
        i+=1
    print(ans+1)
else:
    print(0)

    

