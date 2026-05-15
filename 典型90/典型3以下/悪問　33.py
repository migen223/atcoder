from math import ceil
h,w=map(int,input().split())
H=int(ceil(h/2))
W=int(ceil(w/2))
if h==1 or w==1:
    print(h*w)
else:
    print(H*W)
    
