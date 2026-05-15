n,q=map(int,input().split())
s=list(input())
a=set()
b=set()
c=set()
abc=set()
ans=0
"""
for i in range(n):
    if s[i]=="A":
        a.add(i)
    elif s[i]=="B":
        b.add(i)
    elif s[i]=="C":
        c.add(i)
for i in range(n-2):
    if s[i]=="A" and s[i+1]=="B" and s[i+2]=="C":
        ans+=1
        abc.add(i)
        abc.add(i+1)
        abc.add(i+2)

for i in range(q):
    x,ci=input().split()
    x=int(x)
    if s[x-1]=="A":
        if ci=="A":
            print(ans)
            continue
        else:
            a.remove(x-1)
            if x-1 in abc:
                abc.remove(x-1)
                abc.remove(x)
                abc.remove(x+1)
                ans-=1
            if ci=="B":
                s[x-1]="B"
                b.add(x-1)
                if (x-2 in a) and (x in c):
                    abc.add(x-2)
                    abc.add(x-1)
                    abc.add(x)
                    ans+=1
            elif ci=="C":
                s[x-1]="C"
                c.add(x-1)
                if (x-3 in a) and (x-2 in b):
                    abc.add(x-3)
                    abc.add(x-2)
                    abc.add(x-1)
                    ans+=1
    elif s[x-1]=="B":
        if ci=="B":
            print(ans)
            continue
        else:
            b.remove(x-1)
            if x-1 in abc:
                abc.remove(x-2)
                abc.remove(x-1)
                abc.remove(x)
                ans-=1
            if ci=="A":
                s[x-1]="A"
                a.add(x-1)
                if (x in b) and (x+1 in c):
                    abc.add(x-1)
                    abc.add(x)
                    abc.add(x+1)
                    ans+=1
            elif ci=="C":
                s[x-1]="C"
                c.add(x-1)
                if (x-3 in a) and (x-2 in b):
                    abc.add(x-3)
                    abc.add(x-2)
                    abc.add(x-1)
                    ans+=1
    elif s[x-1]=="C":
        if ci=="C":
            print(ans)
            continue
        else:
            c.remove(x-1)
            if x-1 in abc:
                abc.remove(x-1)
                abc.remove(x-2)
                abc.remove(x-3)
                ans-=1
            if ci=="B":
                s[x-1]="B"
                b.add(x-1)
                if (x-2 in a) and (x in c):
                    abc.add(x-2)
                    abc.add(x-1)
                    abc.add(x)
                    ans+=1
            elif ci=="A":
                s[x-1]="A"
                a.add(x-1)
                if (x in b) and (x+1 in c):
                    abc.add(x-1)
                    abc.add(x)
                    abc.add(x+1)
                    ans+=1
    else:
        if ci=="A":
            s[x-1]="A"
            a.add(x-1)
            if (x in b) and (x+1 in c):
                abc.add(x-1)
                abc.add(x)
                abc.add(x+1)
                ans+=1
        elif ci=="B":
            s[x-1]="B"
            b.add(x-1)
            if (x-2 in a) and (x in c):
                abc.add(x-2)
                abc.add(x-1)
                abc.add(x)
                ans+=1
        elif ci=="C":
            s[x-1]="C"
            c.add(x-1)
            if (x-3 in a) and (x-2 in b):
                abc.add(x-3)
                abc.add(x-2)
                abc.add(x-1)
                ans+=1
    #print(s)
    print(ans)
"""
for i in range(n):
    if s[i]=="A":
        a.add(i)
    elif s[i]=="B":
        b.add(i)
    elif s[i]=="C":
        c.add(i)
for i in range(n-2):
    if s[i]=="A" and s[i+1]=="B" and s[i+2]=="C":
        ans+=1
        abc.add(i)
        abc.add(i+1)
        abc.add(i+2)

for i in range(q):
    x,ci=input().split()
    x=int(x)
    if s[x-1]=="A":
        if ci=="A":
            print(ans)
            continue
        else:
            a.discard(x-1)
            if x-1 in abc:
                abc.discard(x-1)
                abc.discard(x)
                abc.discard(x+1)
                ans-=1
            if ci=="B":
                s[x-1]="B"
                b.add(x-1)
                if (x-2 in a) and (x in c):
                    abc.add(x-2)
                    abc.add(x-1)
                    abc.add(x)
                    ans+=1
            elif ci=="C":
                s[x-1]="C"
                c.add(x-1)
                if (x-3 in a) and (x-2 in b):
                    abc.add(x-3)
                    abc.add(x-2)
                    abc.add(x-1)
                    ans+=1
    elif s[x-1]=="B":
        if ci=="B":
            print(ans)
            continue
        else:
            b.discard(x-1)
            if x-1 in abc:
                abc.discard(x-2)
                abc.discard(x-1)
                abc.discard(x)
                ans-=1
            if ci=="A":
                s[x-1]="A"
                a.add(x-1)
                if (x in b) and (x+1 in c):
                    abc.add(x-1)
                    abc.add(x)
                    abc.add(x+1)
                    ans+=1
            elif ci=="C":
                s[x-1]="C"
                c.add(x-1)
                if (x-3 in a) and (x-2 in b):
                    abc.add(x-3)
                    abc.add(x-2)
                    abc.add(x-1)
                    ans+=1
    elif s[x-1]=="C":
        if ci=="C":
            print(ans)
            continue
        else:
            c.discard(x-1)
            if x-1 in abc:
                abc.discard(x-1)
                abc.discard(x-2)
                abc.discard(x-3)
                ans-=1
            if ci=="B":
                s[x-1]="B"
                b.add(x-1)
                if (x-2 in a) and (x in c):
                    abc.add(x-2)
                    abc.add(x-1)
                    abc.add(x)
                    ans+=1
            elif ci=="A":
                s[x-1]="A"
                a.add(x-1)
                if (x in b) and (x+1 in c):
                    abc.add(x-1)
                    abc.add(x)
                    abc.add(x+1)
                    ans+=1
    else:
        if ci=="A":
            s[x-1]="A"
            a.add(x-1)
            if (x in b) and (x+1 in c):
                abc.add(x-1)
                abc.add(x)
                abc.add(x+1)
                ans+=1
        elif ci=="B":
            s[x-1]="B"
            b.add(x-1)
            if (x-2 in a) and (x in c):
                abc.add(x-2)
                abc.add(x-1)
                abc.add(x)
                ans+=1
        elif ci=="C":
            s[x-1]="C"
            c.add(x-1)
            if (x-3 in a) and (x-2 in b):
                abc.add(x-3)
                abc.add(x-2)
                abc.add(x-1)
                ans+=1
    #print(s)
    print(ans)