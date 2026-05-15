
a,b,c=map(int,input().split())
l=[a,b,c]
l.sort(reverse=True)
print(100*l[0]+10*l[1]+l[2])