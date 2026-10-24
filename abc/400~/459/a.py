

x=int(input())
s="HelloWorld"

for i in range(len(s)):
    if i==x-1:
        continue
    print(s[i],end="")
print()