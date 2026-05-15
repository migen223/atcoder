s=input()
ws=0
cs=["A"]
ans=[]
mod=[]
for i in range(len(s)):
    if s[i]=="W":
        ws+=1
        mod.append("W")
        cs.append("C")
    elif s[i]=="A":
        if ws==0:
            ans.append("A")
        else:
            ans.extend(cs)
            mod=[]
        ws=0
        cs=["A"]
    else:
        ans.extend(mod)
        ans.append(s[i])
        mod=[]
        ws=0
        cs=["A"]
ans.extend(mod)
print("".join(ans))