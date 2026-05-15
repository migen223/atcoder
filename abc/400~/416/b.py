s=input()
t=""
check=1#1の時oがおける
for i in s:
    if i=="#":
        t+="#"
        check=1
    elif i=="." and check==1:
        t+="o"
        check=0
    
    elif i=="." and check==0:
        t+="."
print(t)