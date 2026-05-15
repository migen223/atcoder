
s=input()

t=[]

for i in range(10**5):
    t.append("o")
    t.append("x")
    t.append("x")
t="".join(t)
if s in t:
    print("Yes")
else:
    print("No")

