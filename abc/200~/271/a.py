
n=int(input())
ans=""
h=hex(n)
if h[-2]=="x":
    ans+="0"
else:
    ans+=h[-2]
ans+=h[-1]
print(ans.upper())