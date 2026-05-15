n,q=map(int,input().split())
A=list(map(int,input().split()))
a=[i-1 for i in A]
mas=[0]*n #0は白 1は黒を表す
now=0
for i in range(q):
    if n>1:
        if a[i]==0:
            if mas[a[i]]==0:
                if mas[a[i]+1]==mas[a[i]]:
                    now+=1
            else:
                if mas[a[i]+1]!=mas[a[i]]:
                    now-=1
        elif a[i]==n-1:
            if mas[a[i]]==0:
                if mas[a[i]-1]==mas[a[i]]:
                    now+=1
            else:
                if mas[a[i]-1]!=mas[a[i]]:
                    now-=1
        else:
            if mas[a[i]]==0:
                if mas[a[i]-1]==mas[a[i]+1]==1:
                    now-=1
                elif mas[a[i]-1]==mas[a[i]+1]==0:
                    now+=1
            else:
                if mas[a[i]-1]==mas[a[i]+1]==1:
                    now+=1
                elif mas[a[i]-1]==mas[a[i]+1]==0:
                    now-=1
        if mas[a[i]]==0:
            mas[a[i]]=1
        else:
            mas[a[i]]=0
        #print(mas)
        print(now)
    else:
        
        if i%2==0:
            print(1)
        else:
            print(0)
