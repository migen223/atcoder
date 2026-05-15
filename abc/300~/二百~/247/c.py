
def s(n):
    if n==1:
        return [1]
    else:
        l=[]
        sp=s(n-1)
        for i in sp:
            l.append(i)
        l.append(n)
        for i in sp:
            l.append(i)
        return l
    
print(*s(int(input())))

