from collections import deque
h,w,d=map(int,input().split())
office=[]
senpei=[]
for i in range(w+2):
    senpei.append("#")
office.append(senpei)

for i in range(h):
    l=["#"]
    l.extend(list(input()))
    l.append("#")
    office.append(l)
office.append(senpei)

start=[]
for i in range(1,h+1):
    for j in range(1,w+1):
        if office[i][j]=="H":
            start.append([i,j])
visit=set()
for i in start:
    visit.add(tuple(i))

"""
for i in start:
    stack=[]
    visited=set()
    visited.add(tuple(i))
    #print(i)
    if office[i[0]-1][i[1]]==".":
        stack.append([i[0]-1,i[1]])
    if office[i[0]][i[1]-1]==".":
        stack.append([i[0],i[1]-1])
    if office[i[0]+1][i[1]]==".":
        stack.append([i[0]+1,i[1]])
    if office[i[0]][i[1]+1]==".":
        stack.append([i[0],i[1]+1])
    for j in range(d):
        visitable=[]
        for k in range(len(stack)):
            begin=stack[k]
            visited.add(tuple(stack[k]))
            visit.add(tuple(stack[k]))
            if office[stack[k][0]-1][stack[k][1]]=="." and tuple([stack[k][0]-1,stack[k][1]]) not in visited:
                visitable.append([stack[k][0]-1,stack[k][1]])
            if office[stack[k][0]][stack[k][1]-1]=="." and tuple([stack[k][0],stack[k][1]-1]) not in visited:
                visitable.append([stack[k][0],stack[k][1]-1])
            if office[stack[k][0]+1][stack[k][1]]=="." and tuple([stack[k][0]+1,stack[k][1]]) not in visited:
                visitable.append([stack[k][0]+1,stack[k][1]])
            if office[stack[k][0]][stack[k][1]+1]=="." and tuple([stack[k][0],stack[k][1]+1]) not in visited:
                visitable.append([stack[k][0],stack[k][1]+1])
        stack=visitable
"""
        
stack=start
visited=set()
for i in range(d+1):
    visitable=[]
    for k in range(len(stack)):
        #print(stack)
        
        visited.add(tuple(stack[k]))
        visit.add(tuple(stack[k]))
        if office[stack[k][0]-1][stack[k][1]]=="." and tuple([stack[k][0]-1,stack[k][1]]) not in visited:
            visitable.append([stack[k][0]-1,stack[k][1]])
        if office[stack[k][0]][stack[k][1]-1]=="." and tuple([stack[k][0],stack[k][1]-1]) not in visited:
            visitable.append([stack[k][0],stack[k][1]-1])
        if office[stack[k][0]+1][stack[k][1]]=="." and tuple([stack[k][0]+1,stack[k][1]]) not in visited:
            visitable.append([stack[k][0]+1,stack[k][1]])
        if office[stack[k][0]][stack[k][1]+1]=="." and tuple([stack[k][0],stack[k][1]+1]) not in visited:
            visitable.append([stack[k][0],stack[k][1]+1])
        #print(visitable)
    stack=visitable
print(len(visit))
