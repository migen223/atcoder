h,w,x,y=map(int,input().split())
x-=1
y-=1
town=[]
visited=set()
home=0
for i in range(h):
    town.append(list(input()))
route=list(input())
santa=[x,y]
for i in route:
    if i=="L" and santa[1]!=0:
        if town[santa[0]][santa[1]-1]=="#":
            continue
        elif town[santa[0]][santa[1]-1]==".":
            santa[1]-=1
        elif town[santa[0]][santa[1]-1]=="@":
            santa[1]-=1
            if tuple(santa) in visited:
                continue
            else:
                visited.add(tuple(santa))
                home+=1
    elif i=="R" and santa[1]!=w-1:
        if town[santa[0]][santa[1]+1]=="#":
            continue
        elif town[santa[0]][santa[1]+1]==".":
            santa[1]+=1
        elif town[santa[0]][santa[1]+1]=="@":
            santa[1]+=1
            if tuple(santa) in visited:
                continue
            else:
                visited.add(tuple(santa))
                home+=1
    elif i=="U" and santa[0]!=0:
        if town[santa[0]-1][santa[1]]=="#":
            continue
        elif town[santa[0]-1][santa[1]]==".":
            santa[0]-=1
        elif town[santa[0]-1][santa[1]]=="@":
            santa[0]-=1
            if tuple(santa) in visited:
                continue
            else:
                visited.add(tuple(santa))
                home+=1
    elif i=="D" and santa[0]!=h-1:
        if town[santa[0]+1][santa[1]]=="#":
            continue
        elif town[santa[0]+1][santa[1]]==".":
            santa[0]+=1
        elif town[santa[0]+1][santa[1]]=="@":
            santa[0]+=1
            if tuple(santa) in visited:
                continue
            else:
                visited.add(tuple(santa))
                home+=1
    #print(santa)
print(santa[0]+1,santa[1]+1,home)

