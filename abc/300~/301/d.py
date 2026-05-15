
s=list(input())
n=int(input())
ans=0
kouho=[]
for i in range(len(s)):
    if s[-i-1]=="1":
        ans+=2**i

def solve(s,n):
    for i in range(len(s)):
        #print(s)
        if s[i]=="?":
            
            s[i]="1"
            ns=[]
            for j in range(len(s)):
                if s[j]=="?":
                    ns.append("0")
                else:
                    ns.append(s[j])
            if int("".join(ns),2)>n:
                s[i]="0"
            else:
                continue
            #print("".join(ns))
    return int("".join(s),2)


if ans>n:
    print(-1)
elif ans==n:
    print(ans)
else:
    print(solve(s,n))




"""
n=format(int(input()),'b')

if len(s)<len(n):
    for i in range(len(s)):
        if s[i]=="?":
            s[i]="1"
    print(int("".join(s),2))
elif len(s)==len(n):
    f=0
    for i in range(len(s)):
        if s[i]=="?":
            if n[i]=="1":
                s[i]="1"
            else:
                if f==0:
                    s[i]="0"
                else:
                    s[i]="1"
        elif s[i]=="1":
            if n[i]=="0":
                if f==0:
                    print(-1)
                    sys.exit()
        elif s[i]=="0":
            if n[i]=="1":
                f+=1
    #print(s)
    print(int("".join(s),2))
else:
    s=deque(s)
    for i in range(len(s)-len(n)):
        now=s.popleft()
        if now=="1":
            print(-1)
            sys.exit()
    s=list(s)
    f=0
    for i in range(len(s)):
        if s[i]=="?":
            if n[i]=="1":
                s[i]="1"
            else:
                if f==0:
                    s[i]="0"
                else:
                    s[i]="1"
        elif s[i]=="1":
            if n[i]=="0":
                if f==0:
                    print(-1)
                    sys.exit()
        elif s[i]=="0":
            if n[i]=="1":
                f+=1
    #print(s)
    print(int("".join(s),2))


"""