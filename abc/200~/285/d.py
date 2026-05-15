import sys
n=int(input())

dic={}
se=set()
graph=[]
count=0
for i in range(n):
    s,t=input().split()
    if s not in se:
        dic[s]=count
        count+=1
        se.add(s)
        graph.append([])
    if  t not in se:
        dic[t]=count
        count+=1
        se.add(t)
        graph.append([])
    graph[dic[s]].append(dic[t])

visit=set()
for i in range(len(graph)):
    if i not in visit:
        route=set()
        route.add(i)
        visitable=[[i,route]]
        while visitable:
            now=visitable.pop()
            visit.add(now[0])
            for j in graph[now[0]]:
                #print(j)
                if j not in now[1]:
                    now[1].add(j)
                    visitable.append([j,now[1]])
                else:
                    print("No")
                    sys.exit()
print("Yes")


    

    
