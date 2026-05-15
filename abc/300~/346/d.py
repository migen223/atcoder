
n=int(input())
s=input()
c=list(map(int,input().split()))
s01=[]
s10=[]
def swap(n):
    if n==1:
        return "0"
    else:
        return "1"
    
l01=["0","1"]
l10=["1","0"]
for i in range(n):
    l01.append("0")
    l01.append("1")
    l10.append("1")
    l10.append("0")

if s[0]=="1":
    s01.append(c[0])
    s10.append(0)
else:
    s10.append(c[0])
    s01.append(0)
for i in range(1,n):
    if s[i]=="0" and i%2==0:
        s01.append(s01[-1])
        s10.append(s10[-1]+c[i])
    elif s[i]=="0" and i%2==1:
        s01.append(s01[-1]+c[i])
        s10.append(s10[-1])
    elif s[i]=="1" and i%2==0:
        s01.append(s01[-1]+c[i])
        s10.append(s10[-1])
    else:
        s01.append(s01[-1])
        s10.append(s10[-1]+c[i])

if n!=2:
    ans=10**18
    for i in range(n-1):
        for j in range(2):
            now=0
            if s[i]!=str(j):
                now+=c[i]
            if s[i+1]!=str(j):
                now+=c[i+1]
            if i==0:
                if swap(j)==l01[i+2]:
                    now+=s01[-1]-s01[i+1]
                else:
                    now+=s10[-1]-s10[i+1]
            elif i==n-1:
                if swap(j)==l01[i-1]:
                    now+=s01[i-1]
                else:
                    now+=s10[i-1]
            else:
                if swap(j)==l01[i+2]:
                    now+=s01[-1]-s01[i+1]
                else:
                    now+=s10[-1]-s10[i+1]
                if swap(j)==l01[i-1]:
                    now+=s01[i-1]
                else:
                    now+=s10[i-1]
            ans=min(now,ans)
else:
    ans=10**18
    for i in range(2):
        now=0
        for j in range(2):
            if s[j]!=str(i):
                now+=c[j]
        ans=min(now,ans)
print(ans)

                



