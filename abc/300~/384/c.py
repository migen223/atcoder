a,b,c,d,e=map(int,input().split())
dic={}
people=['ABCDE', 'BCDE', 'ACDE', 'ABDE', 'ABCE', 'ABCD', 'CDE', 'BDE', 'ADE', 'BCE', 'ACE', 'BCD', 'ABE', 'ACD', 'ABD', 'ABC', 'DE', 'CE', 'BE', 'CD', 'AE', 'BD', 'AD', 'BC', 'AC', 'AB', 'E', 'D', 'C', 'B', 'A']
score=[]
for i in range(31):
    sc=0
    for j in range(len(people[i])):
        if people[i][j]=="A":
            sc+=a
        elif people[i][j]=="B":
            sc+=b
        elif people[i][j]=="C":
            sc+=c
        elif people[i][j]=="D":
            sc+=d
        else:
            sc+=e
    score.append(sc)
    if sc in dic:
        dic[sc].append(people[i])
        dic[sc].sort()
    else:
        dic[sc]=[people[i]]
score.sort(reverse=True)
for i in range(len(dic[score[0]])):
    print(dic[score[0]][i])
for i in range(1,31):
    if score[i]==score[i-1]:
        continue
    for j in range(len(dic[score[i]])):
        print(dic[score[i]][j])
    