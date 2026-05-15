a,b,c,d=map(int,input().split())
if a==c:
    if b>d:
        print("Aoki")
    else:
        print("Takahashi")
elif a<c:
    print("Takahashi")
else:
    print("Aoki")