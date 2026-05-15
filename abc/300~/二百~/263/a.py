
from collections import Counter
a=list(map(int,input().split()))
c=Counter(a)
#print(c.most_common(2))
if len(c)>=2:
    if c.most_common(2)[0][1]==3 and c.most_common(2)[1][1]==2:
        print("Yes")
    else:
        print("No")
else:
    print("No")