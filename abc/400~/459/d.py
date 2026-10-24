from collections import Counter
import heapq
t=int(input())

for _ in range(t):
    s=input()
    n=len(s)
    c=Counter(s)
    #print(c)
    ans=[]
    ss=[]
    for ci in c:
        ss.append([ci,c[ci]])
    ss.sort(key=lambda x:x[1])
    #print(ss)
    if len(ss)==1:
        if n==1:
            print("Yes")
            print(s)
        else:
            print("No")
        continue
    hq=[]
    for i in range(len(ss)):
        heapq.heappush(hq,(-ss[i][1],ss[i][0]))
    #print(hq)
    if n%2==0:
        if ss[-1][1]<=n//2 and ss[-2][1]<=n//2:
            while hq:
                on,os=heapq.heappop(hq)
                tn,ts=heapq.heappop(hq)
                ans.append(str(os))
                ans.append(str(ts))
                on+=1
                tn+=1
                if on!=0:
                    heapq.heappush(hq,(on,os))
                if tn!=0:
                    heapq.heappush(hq,(tn,ts))
                if len(hq)==1:
                    ans.append(hq[0][1])
                    break
            print("Yes")
            print("".join(ans))
        else:
            print("No")
    else:
        if ss[-1][1]<=(n+1)//2 and ss[-2][1]<=n//2:
            while hq:
                on,os=heapq.heappop(hq)
                tn,ts=heapq.heappop(hq)
                ans.append(str(os))
                ans.append(str(ts))
                on+=1
                tn+=1
                if on!=0:
                    heapq.heappush(hq,(on,os))
                if tn!=0:
                    heapq.heappush(hq,(tn,ts))
                if len(hq)==1:
                    ans.append(hq[0][1])
                    break
            print("Yes")
            print("".join(ans))
        else:
            print("No")

"""
    if n%2==0:
        if ss[-1][1]<=n//2 and ss[-2][1]<=n//2:
            f=0
            while ss:
                ans.append(str(ss[-1][0]))
                ans.append(str(ss[-2][0]))
                ss[-1][1]-=1
                ss[-2][1]-=1
                ban=[0,0,0]
                if ss[-1][1]==0:
                    ban[1]=1
                if ss[-2][1]==0:
                    ban[2]=1
                if ban[1]==1 and ban[2]==1:
                    ss.pop()
                    ss.pop()
                elif ban[1]==1 and ban[2]==0:
                    ss.pop()
                elif ban[1]==0 and ban[2]==1:
                    save=ss.pop()
                    ss.pop()
                    ss.append(save)
 
                    if len(ss)==1:
                        if ss[-1][1]==1:
                            ans.append(str(ss[-1][0]))
                            break
                print(ss)
            if f==0:
                print("Yes")
                print("".join(ans))
        else:
            print("No")
    else:
        if ss[-1][1]<=(n+1)//2 and ss[-2][1]<=n//2:
            f=0
            while ss:
                ans.append(str(ss[-1][0]))
                ans.append(str(ss[-2][0]))
                ss[-1][1]-=1
                ss[-2][1]-=1
                ban=[0,0,0]
                if ss[-1][1]==0:
                    ban[1]=1
                if ss[-2][1]==0:
                    ban[2]=1
                if ban[1]==1 and ban[2]==1:
                    ss.pop()
                    ss.pop()
                elif ban[1]==1 and ban[2]==0:
                    ss.pop()
                elif ban[1]==0 and ban[2]==1:
                    save=ss.pop()
                    ss.pop()
                    ss.append(save)
                if len(ss)==1:
                    if ss[-1][1]==1:
                        ans.append(str(ss[-1][0]))
                        break
                print(ss)
            if f==0:
                print("Yes")
                print("".join(ans))
        else:
            print("No")

"""