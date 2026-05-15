
n=int(input())
s=list(input())
f=0
for i in range(n):
    if f==0 and s[i]=='"':
        f=1
    elif f==1 and s[i]=='"':
        f=0
    elif f==0 and s[i]==",":
        s[i]="."
print("".join(s))