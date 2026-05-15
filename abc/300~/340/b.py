q=int(input())
a=[]
for i in range(q):
    que=input().split()
    if que[0]=="1":
        a.append(int(que[1]))
    else:
        print(a[-int(que[1])])