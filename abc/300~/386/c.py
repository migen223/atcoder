import sys
k=int(input())
s=list(input())
t=list(input())
if s==t:
    print("Yes")
else:
    if len(s)+1==len(t):#挿入するとき
        f=0
        count=0
        for i in range(len(s)+1):
            if f==0 and i!=len(s):
                if s[i]!=t[i]:
                    f+=1
                    continue
            elif f==0 and i==len(s):
                print("Yes")
                sys.exit()
            else:
                if s[i-1]!=t[i]:
                    print("No")
                    sys.exit()
        print("Yes")
    elif len(s)==len(t):#１文字変える時
        difference=0
        for i in range(len(s)):
            if s[i]!=t[i]:
                difference+=1
        if difference==1:
            print("Yes")
        else:
            print("No")
    elif len(s)==len(t)+1:#１文字消す時
        f=0
        count=0
        for i in range(len(t)+1):
            if f==0 and i!=len(t):
                if t[i]!=s[i]:
                    f+=1
                    continue
            elif f==0 and i==len(t):
                print("Yes")
                sys.exit()
            else:
                if t[i-1]!=s[i]:
                    print("No")
                    sys.exit()
        print("Yes")
    else:
        print("No")

