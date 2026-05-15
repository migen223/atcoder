
n,m=map(int,input().split())
s=input()
t=input()
q=int(input())
taka=set(list(s))
ao=set(list(t))


for i in range(q):
    w=set(list(input()))
    if len(w&taka)==len(w) and len(w&ao)!=len(w):
        print("Takahashi")
    elif len(w&ao)==len(w) and len(w&taka)!=len(w):
        print("Aoki")
    else:
        print("Unknown")