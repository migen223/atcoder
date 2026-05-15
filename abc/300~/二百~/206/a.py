from math import floor
n=int(input())

x=floor(1.08*n)
if x<206:
    print("Yay!")
elif x>206:
    print(":(")
else:
    print("so-so")