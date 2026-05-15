from sortedcontainers import SortedList

n,k=map(int,input().split())
p=list(map(int,input().split()))

cards=SortedList([])
parents={}
dic={}
ans=[-1]*n

if k>=2:
    for i in range(n):
        if len(cards)==0:
            cards.add(p[i])
            parents[p[i]]=p[i]
            dic[p[i]]=[p[i]]
        else:
            ind=cards.bisect_left(p[i])
            if ind==len(cards):
                cards.add(p[i])
                parents[p[i]]=p[i]
                dic[p[i]]=[p[i]]
            else:
                card=cards[ind]
                parent=parents[card]
                parents[p[i]]=parent
                cards.remove(card)
                cards.add(p[i])
                dic[parent].append(p[i])
                if len(dic[parent])==k:
                    #print(i,dic,p[i],parent,ind,"card",card)
                    for j in dic[parent]:
                        ans[j-1]=i+1
                    cards.remove(p[i])

        #print(i)
        #print(cards)
        #print("parents",parents)
        
else:
    for i in range(n):
        ans[p[i]-1]=i+1
#print(dic)
for i in range(n):
    print(ans[i])