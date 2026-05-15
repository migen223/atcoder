
n,k=map(int,input().split())

stu=[list(map(int,input().split())) for i in range(n)]

scores=[sum(stu[i]) for i in range(n)]

ssort=sorted(scores,reverse=True)

kscore=ssort[k-1]



for i in range(n):
    if scores[i]+300>=kscore:
        print("Yes")
    else:
        print("No")