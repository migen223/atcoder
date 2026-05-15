a=list(map(int,input().split()))
for i in range(8):
    an=a[i]+a[i+1]
    if an<10:
        a.append(an)
    else:
        p=""
        char=str(an)
        for j in range(len(str(char))-1,-1,-1):
            p+=char[j]
        a.append(int(p))
print(a[-1])
            