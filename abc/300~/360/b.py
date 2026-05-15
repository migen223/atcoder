import sys
s,t=input().split()
if len(s)==1:
    print("No")
else:

    for w in range(1,len(s)):
        for c in range(w):
            word=""
            if len(s)%w==0:
                for i in range(len(s)//w):   
                    word+=s[c+i*w]
                if word==t:
                    print("Yes")
                    sys.exit()
            else:
                for i in range(len(s)//w+1):
                    if c+i*w<len(s):
                        word+=s[c+i*w]
                if word==t:
                    print("Yes")
                    sys.exit()
    print("No")