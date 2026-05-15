import sys
w,b=map(int,input().split())
origin="wbwbwwbwbwbw"
s=""
for i in range(16):
    s+=origin
s+="wbwbwwbw"
for i in range(200-(w+b)+1):
    bn=0
    wn=0
    for j in range(w+b):
        if s[i+j]=="w":
            wn+=1
        else:
            bn+=1
    if bn==b and wn==w:
        print("Yes")
        sys.exit()
print("No")