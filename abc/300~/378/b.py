n=int(input())
day=[]
for i in range(n):
    day.append(list(map(int,input().split())))
q=int(input())
for i in range(q):
    t,d=map(int,input().split())
    plus=(day[t-1][1]-d)%(day[t-1][0])
    print(d+plus)