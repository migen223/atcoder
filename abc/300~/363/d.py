
n=int(input())
if n>19:
    k=9
    num=19
    l=[10,9]
    while num<n:
        k*=10
        num+=2*k
        l.append(k)
        l.append(k)
        if num>=n:
            break
    r=[l[0]]
    for i in range(1,len(l)):
        r.append(r[-1]+l[i])
    #print(r)
    keta=0
    for i in range(len(l)):
        if r[i]>=n:
            keta=i+1
            break
    #print(keta)
    ord=n-r[keta-2]
    #print(ord)

    ans=[0]*keta

    now=0
    kind=(keta+1)//2
    for i in range(kind):
    # print("i",i)
        if i==0:
            for j in range(1,10):
                if now+10**(kind-1-i)>=ord:
                    
                    ans[i]=str(j)
                    ans[-1-i]=str(j)
                    #print("j",j,"now",now)
                    break
                else:
                    now+=10**(kind-1-i)
                #print("j",j,"now",now)
        else:
            for j in range(10):
                if now+10**(kind-1-i)>=ord:
                    ans[i]=str(j)
                    ans[-i-1]=str(j)
                    
                    break
                else:
                    now+=10**(kind-1-i)
                #print("j",j,"now",now)
        #print("now",now)
        #print("ans",ans)

    print("".join(ans))
else:
    l=[0,1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]
    print(l[n-1])





