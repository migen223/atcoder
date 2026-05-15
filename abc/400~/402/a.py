s=input()
char=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ans=""
for a in s:
    for i in char:
        if i==a:
            ans+=a
print(ans)