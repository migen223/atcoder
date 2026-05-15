

"""
sr=[0,s[0]]
for i in range(1,n):
    sr.append(sr[-1]+s[i])

minl=[]
for i in range(n):
    if t[i]==mi:
        minl.append(i)
se=set(minl)


for i in range(len(minl)):
    k=1
    while minl[i]+k not in se and minl[i]+k<=n-1:
        ans[minl[i]+k]=min(ans[minl[i]+k],t[minl[i]]+sr[minl[i]+k]-sr[minl[i]])
        k+=1
        k%=n

for i in range(n):
    print(ans[i])
"""

