n,k=map(int,input().split())
point=[]
for i in range(n):
    a,b=map(int,input().split())
    point.append(b)
    point.append(a-b)
point.sort(reverse=True)
score=0
for i in range(k):
    score+=point[i]
print(score)