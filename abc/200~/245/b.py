n=int(input())
a=list(map(int,input().split()))
se=set(a)
for i in range(2001):
    if i not in se:
        print(i)
        break