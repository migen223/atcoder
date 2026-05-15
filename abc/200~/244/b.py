
n=int(input())
t=input()
dy=[0,-1,0,1]
dx=[1,0,-1,0]
now=[0,0]
dir=0
for i in range(n):
    if t[i]=="S":
        now[0]+=dx[dir]
        now[1]+=dy[dir]
    else:
        dir=(dir+1)%4

print(*now)


