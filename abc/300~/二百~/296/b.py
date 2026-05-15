grid=[list(input()) for i in range(8)]
line={0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h"}
for i in range(8):
    for j in range(8):
        if grid[i][j]=="*":
            
            print(line[j],end="")
            print(8-i)
            break