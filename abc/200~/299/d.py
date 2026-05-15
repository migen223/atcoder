import sys
n=int(input())

l=1
r=n

while True:
    print(f"? {(l+r)//2}")
    s=int(input())
    if s==0:
        l=(l+r)//2
    else:
        r=(l+r)//2
    if l+1==r:
        print(f"! {l}")
        sys.exit()