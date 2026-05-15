import bisect
n=int(input())
i=input()
al=list(map(int,i.split()))
al.sort()
q=int(input())
"""
for a in range(q):
    b=int(input())
    l=0
    h=len(al)-1
    while True:
        k=int((l+h)/2)
        if k==len(al)-1:
            print(abs(al[len(al)-1]-b))
            break
        if h<0:
            print(abs(al[0]-b))
            break
        if (al[k+1]-b)*(al[k]-b)<=0:
            if abs(al[k]-b)<abs(al[k+1]-b):
                print(abs(al[k]-b))
                break
            else:
                print(al[k+1]-b)
                break
        else:
            if b<al[k]:
                h=k-1
            else:
                l=k+1
"""

for _ in range(q):
    b=int(input())
    idx=bisect.bisect_left(al,b)
    kouho=[]
    if idx<n:
        kouho.append(abs(al[idx]-b))
    if idx>0:
        kouho.append(abs(al[idx-1]-b))
    print(min(kouho))




    