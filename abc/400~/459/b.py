
n=int(input())
s=input().split()

se=[[],[],set(["a","b","c"]),set(["d","e","f"]),set(["g","h","i"]),set(["j","k","l"]),set(["m","n","o"]),set(["p","q","r","s"]),set(["t","u","v"]),set(["w","x","y","z"])]

ans=[]
for i in range(n):
    si=s[i]
    for j in range(10):
        if si[0] in se[j]:
            ans.append(str(j))
            break

print("".join(ans))