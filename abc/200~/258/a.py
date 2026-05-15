
k=int(input())
h=k//60
m=k%60
#print(m)
if m<=9:

    print(f"{21+h}:0{m}")
else:
    print(f"{21+h}:{m}")