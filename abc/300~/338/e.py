import sys
n=int(input())

edge=[]
li={}
ri={}
for i in range(n):
    a,b=map(int,input().split())
    l,r=sorted([a,b])
    edge.append((l,r))
    li[l]=i
    ri[r]=i

stack=[]
for i in range(1,2*n):
    if i in li:
        stack.append(li[i])
    else:
        ind=ri[i]
        last=stack.pop()
        if ind != last:
            print("Yes")
            sys.exit()
print("No")


"""
3
1 2
3 6
4 5

4
2 3
1 4
5 8
6 7

"""