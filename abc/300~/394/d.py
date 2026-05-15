import sys
s=list(input())
cir=0
squ=0
tri=0
for i in range(len(s)):
    if s[i]=="(":
        cir+=1
    elif s[i]==")":
        cir-=1
    elif s[i]=="[":
        squ+=1
    elif s[i]=="]":
        squ-=1
    elif s[i]=="<":
        tri+=1
    elif s[i]==">":
        tri-=1
    if cir<0 or tri<0 or squ<0:
        print("No")
        sys.exit()

kakko=[]
if cir + tri + squ > 0:
    print("No")
else:
    for i in range(len(s)):
        if s[i]=="(" or s[i]=="[" or s[i]=="<":
            kakko.append(s[i])
        elif s[i]==")":
            if kakko.pop()=="(":
                continue
            else:
                print("No")
                sys.exit()
        elif s[i]=="]":
            if kakko.pop()=="[":
                continue
            else:
                print("No")
                sys.exit()
        elif s[i]==">":
            if kakko.pop()=="<":
                continue
            else:
                print("No")
                sys.exit()
    print("Yes")
            