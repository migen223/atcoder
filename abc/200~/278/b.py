h,m=input().split()
if len(h)==1:
    h="0"+h

if len(m)==1:
    m="0"+m

def zero(s):
    if len(s)==1:
        return "0"+s
    else:
        return s
    
def step(h,m):
    if m+1==60:
        if h+1==24:
            return [0,0]
        else:
            return [h+1,0]
    else:
        return [h,m+1]
    
def check(h,m):
    ho=int(h[0]+m[0])
    mi=int(h[1]+m[1])
    if ho>23 or mi>59:
        return False
    else:
        return True
for i in range(1000):
    if check(h,m):
        print(h,m)
        break
    else:
        l=step(int(h),int(m))
        h=zero(str(l[0]))
        m=zero(str(l[1]))
    