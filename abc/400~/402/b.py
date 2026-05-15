q=int(input())
row=[]
for i in range(q):
    i=input()
    l=list(map(int,i.split()))
    if l[0]==1:
        row.append(l[1])
    else:
        print(row.pop(0))
