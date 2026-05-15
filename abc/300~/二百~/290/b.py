n,k=map(int,input().split())
s=list(input())

for i in range(n):
    #print(k)
    if s[i]=="o":
        if k!=0:
            k-=1
        else:
            s[i]="x"
    else:
        s[i]="x"
    
print("".join(s))
