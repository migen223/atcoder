import sys
h,w=map(int,input().split())
grid=[]
for i in range(h):
    grid.append(list(input()))
if w>=2 and h>=2:
    for i in range(h):
        for j in range(w):
            if grid[i][j]=="#":
                count=0
                if i==0:
                    if j==0:
                        if grid[1][0]==grid[0][1]=="#":
                            continue
                        else:
                            #print(i,j)
                            print("No")
                            sys.exit()
                    elif j==w-1:
                        if grid[0][w-2]==grid[1][w-1]=="#":
                            continue
                        else:
                            #print(i,j)
                            print("No")
                            sys.exit()
                        
                    else:
                        if grid[0][j-1]=="#":
                            count+=1
                        if grid[0][j+1]=="#":
                            count+=1
                        if grid[1][j]=="#":
                            count+=1
                        if count!=2:
                            #print(i,j)
                            print("No")
                            sys.exit()
                elif i==h-1:
                    if j==0:
                        if grid[h-2][0]==grid[h-1][1]=="#":
                            continue
                        else:
                            #print(i,j)
                            print("No")
                            sys.exit()
                    elif j==w-1:
                        if grid[h-1][w-2]==grid[h-2][w-1]=="#":
                            continue
                        else:
                            #print(i,j)
                            print("No")
                            sys.exit()
                    else:
                        if grid[h-1][j-1]=="#":
                            count+=1
                        if grid[h-1][j+1]=="#":
                            count+=1
                        if grid[h-2][j]=="#":
                            count+=1
                        if count!=2:
                            #print(i,j)
                            print("No")
                            sys.exit()
                else:
                    if j==0:
                        if grid[i][1]=="#":
                            count+=1
                        if grid[i-1][0]=="#":
                            count+=1
                        if grid[i+1][0]=="#":
                            count+=1
                        if count!=2:
                            #print(i,j)
                            print("No")
                            sys.exit()
                    elif j==w-1:
                        if grid[i][w-2]=="#":
                            count+=1
                        if grid[i-1][w-1]=="#":
                            count+=1
                        if grid[i+1][w-1]=="#":
                            count+=1
                        if count!=2:
                            #print(i,j)
                            print("No")
                            sys.exit()
                    else:
                        if grid[i][j-1]=="#":
                            count+=1
                        if grid[i][j+1]=="#":
                            count+=1
                        if grid[i-1][j]=="#":
                            count+=1
                        if grid[i+1][j]=="#":
                            count+=1
                        if count==2 or count==4:
                            continue
                        else:
                            #print(i,j)
                            print("No")
                            sys.exit()
    print("Yes")
else:
    for i in range(h):
        for j in range(w):
            if grid[i][j]=="#":
                print("No")
                sys.exit()
    print("Yes")
