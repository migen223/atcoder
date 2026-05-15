
h1,h2,h3,w1,w2,w3=map(int,input().split())

ans=0

for i in range(1,29):
    for j in range(1,29):
        for k in range(1,29):
            for l in range(1,29):
                a02=h1-i-j
                a12=h2-k-l
                a20=w1-i-k
                a21=w2-j-l
                if a02>0 and a12>0 and a20>0 and a21>0:
                    a22=h3-a20-a21
                    if a22+a12+a02==w3 and a22>0:
                        ans+=1
                        #print(i,j,a02)
                        #print(k,l,a12)
                        #print(a20,a21,a22)
                        #print()

print(ans)