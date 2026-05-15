import sys
n,m=map(int,input().split())
b=list(map(int,input().split()))
w=list(map(int,input().split()))
b.sort(reverse=True)
w.sort(reverse=True)
bcum=[b[0]]
wcum=[w[0]]
nowb=b[0]
noww=w[0]
for i in range(1,n):
    nowb+=b[i]
    bcum.append(nowb)
for i in range(1,m):
    noww+=w[i]
    wcum.append(noww)

#print(bcum)
#print(wcum)
bind0=n #負になる初めてインデックス
for i in range(n):
    if b[i]<0:
        bind0=i
        break
wind0=m
for i in range(m):
    #print(w[i])
    if w[i]<0:
         wind0=i
         break

if n<=m:#白の方が多い時
    if bind0>=wind0:
        if bind0==0:
            print(0)
        else:
            if wind0==0:
                print(bcum[bind0-1])
            else:
                print(bcum[bind0-1]+wcum[wind0-1])
    else:
        wplus=n#何個白玉を加えるか
        for i in range(n):
            if w[0]+b[0]<0:
                print(0)
                sys.exit()
            else:
                if w[i]+b[i]<0:
                    wplus=i
                    break
        print(wcum[wplus-1]+bcum[wplus-1])

else:#黒の方が多い
    if bind0>=wind0:
        if bind0==0:
            print(0)
        else:
            #print(f"{bcum[bind0-1]}+{wcum[wind0-1]}")
            if wind0==0:
                print(bcum[bind0-1])
            else:
                print(bcum[bind0-1]+wcum[wind0-1])
    else:
        wplus=m#何個白玉を加えるか
        for i in range(m):
            if w[0]+b[0]<0:
                print(0)
                sys.exit()
            else:
                if w[i]+b[i]<0:
                    wplus=i
                    break
                
        print(wcum[wplus-1]+bcum[wplus-1])