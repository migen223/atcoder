from collections import deque
from sortedcontainers import SortedSet
import heapq
import sys
n,k=map(int,input().split())

h=[]
dic={}
now=0
time=0
for i in range(n):
    a,b,c=map(int,input().split())
    if len(h)>=1:
        while a>=h[0]:
            cus=heapq.heappop(h)
            now-=dic[cus]
            dic.pop(cus)
            if len(dic)==0 or len(h)==0:
                #print(dic,h)
                break
    
    if now+c<=k:
        now+=c
        if time>a:
            print(time)
            if time+b in dic:
                dic[time+b]+=c
               
            else:
                dic[time+b]=c
                heapq.heappush(h,time+b)
        else:
            print(a)
            if a+b in dic:
                dic[a+b]+=c
            else:
                dic[a+b]=c
                heapq.heappush(h,a+b)
    else:
        while now+c>k:
            time=heapq.heappop(h)
            now-=dic[time]
            dic.pop(time)
            if len(dic)==0:
                break
        now+=c
        print(time)
        if time+b in dic:
            dic[time+b]+=c

        else:
            dic[time+b]=c
            heapq.heappush(h,time+b)

"""
que=deque([])
eat=SortedSet([])
dic={}
now=0
last=0
for i in range(n):
    a,b,c=tuple(map(int,input().split()))
    if now+c<=k:
        if last==0:
            print(a)
            now+=c
            if a+b in dic:
                dic[a+b]+=c
            else:
                eat.add(a+b)
                dic[a+b]=c
        else:
            if last>a:
                print(last)
                now+=c
                if last+b in eat:
                    dic[last+b]+=c
                else:
                    eat.add(last+b)
                    dic[last+b]=c
            else:
                print(a)
                now+=c
                if a+b in dic:
                    dic[a+b]+=c
                else:
                    dic[a+b]=c
    else:
        if eat[0]<a:
            while len(eat)>=1 and eat[0]<a:
                cus=eat.pop(0)
                if cus in dic:
                    now-=dic[cus]
                    dic.pop(cus)
        if now+c<=k:
            print(a)
            now+=c
            if a+b in dic:
                dic[a+b]+=c
            else:
                eat.add(a+b)
                dic[a+b]=c
        else:
            while now+c>k and len(eat)>=1:
                cus=eat.pop(0)
                last=cus
                if cus in dic:
                    now-=dic[cus]
                    dic.pop(cus)
            print(cus)
            now+=c
            if last+b in dic:
                dic[last+b]+=c
            else:
                eat.add(last+b)
                dic[last+b]=c
    #print(eat)
    #print(dic)
"""