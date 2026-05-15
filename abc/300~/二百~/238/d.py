
t=int(input())

for i in range(t):
    a,s=map(int,input().split())
    if s-2*a>=0 and (s-2*a)&(a)==0:
        print("Yes")
    else:
        print("No")

"""
def keta(n):
    count=0
    while 2**(count+1)<=n:
        count+=1
    return count+1

def ten_to_n(num,n):#numをn進数に変換　返り値はstr
    if num==0:
        return "0"
    else:
        k=0
        while n**k<=num:
            k+=1
        ans=[]
        rang=k
        for i in range(rang):
            k-=1
            keta=num//(n**k)
            num-=keta*(n**k)
            ans.append(str(keta))
        return "".join(ans) 

for i in range(t):
    a,s=map(int,input().split())
    if s-2*a<0:
        print("No")
    elif s==2*a:
        print("Yes")
    else:

    
        an=keta(a)
        sn=keta(s)
        k=max(an,sn)
        a2=ten_to_n(a,2)
        use=[]
        se=set()
        for j in range(len(a2)):
            if a2[j]!="1":
                use.append(2**(len(a2)-j-1))
                se.add(2**(len(a2)-j-1))
        for j in range(an,sn):
            use.append(2**j)
            se.add(2**j)
        need=s-2*a
        f=0
        #print(a2)
        print(use)
        for j in range(len(use)):
            if need==2*use[j]:
                continue
            if need-use[j]<0:
                print("No")
                f+=1
                break
            if need==use[j]:
                print("Yes")
                f+=1
                break
            if need-use[j] in se:
                print("Yes")
                f+=1
                break
        if f==0:
            print("No")
        """
    
    

