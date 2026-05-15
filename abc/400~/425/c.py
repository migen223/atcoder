n,q=map(int,input().split())
a=list(map(int,input().split()))
roop=[]
for i in range(n):
    roop.append(a[i])
for i in range(n-1):
    roop.append(a[i])
ruiseki=[]
s=0
for i in range(len(roop)):
    s+=roop[i]
    ruiseki.append(s)
offset=0
for i in range(q):
    que=input().split()

    if que[0]=="1":
        offset=(offset+int(que[1]))%n
    else:
        l=int(que[1])-1
        r=int(que[2])-1
        if l==0 and offset==0:
            print(ruiseki[r])
        else:
            #print(r+offset,l+offset)
            print(ruiseki[r+offset]-ruiseki[l+offset-1])