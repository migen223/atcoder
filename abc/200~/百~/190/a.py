a,b,c=map(int,input().split())
while True:
    if c==0:
        a-=1
        if a<0:
            print("Aoki")
            break
        b-=1
        if b<0:
            print("Takahashi")
            break
    else:
        b-=1
        if b<0:
            print("Takahashi")
            break
        a-=1
        if a<0:
            print("Aoki")
            break
"""
if c==0:
    if a>b:
        print("Takahashi")
    else:
        print("Aoki")
else:
    if a>b:
        print("Aoki")
    else:
        print("Takahashi")
        """