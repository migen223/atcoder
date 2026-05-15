from itertools import permutations
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a3=list(map(int,input().split()))
dice=[a1,a2,a3]
ue=0
sita=6**3

l=[4,5,6]
for p in permutations([4,5,6]):
    #print(p)
    count=[0,0,0]
    for j in range(3):
        for k in range(6):
            if dice[j][k]==p[j]:
                count[j]+=1
    ue+=count[0]*count[1]*count[2]
    
print(ue/sita)