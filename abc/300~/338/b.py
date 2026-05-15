s=input()
dic={}
dic2={}
kind=[0]*26
count=0
for i in range(97, 123):
    dic[chr(i)]=count
    dic2[count]=chr(i)
    count+=1
for i in range(len(s)):
    kind[dic[s[i]]]+=1
ma=max(kind)
for i in range(len(kind)):
    if kind[i]==ma:
        print(dic2[i])
        break

