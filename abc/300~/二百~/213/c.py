
h,w,n=map(int,input().split())
cards=[list(map(int,input().split())) for i in range(n)]

xse=set()
yse=set()
for i in range(n):
    xse.add(cards[i][1])
    yse.add(cards[i][0])
xl=list(xse)
yl=list(yse)
xl.sort()
yl.sort()

dicx={}
dicy={}
for i in range(len(xl)):
    dicx[xl[i]]=i
for i in range(len(yl)):
    dicy[yl[i]]=i

for i in range(n):
    print(dicy[cards[i][0]]+1,dicx[cards[i][1]]+1)
