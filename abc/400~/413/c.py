q=int(input())
a=[]
offset=0
for _ in range(q):
    que=list(map(int,input().split()))
    if que[0]==1:
        l=[que[1],que[2]]
        a.append(l)
    else:
        t=que[1]
        ans=0
        while t>0:
            for i in range(offset,len(a)):
                #if a[0]==0:
                    #continue
                #else:
                    if t>=a[i][0]:
                        t-=a[i][0]
                        ans+=a[i][0]*a[i][1]
                        a[i][0]=0
                        offset+=1
                        #print(a,t,ans)
                    else:
                        ans+=t*a[i][1]
                        a[i][0]-=t
                        t=0
                        #print(a,t,ans)
                        break
        print(ans)
