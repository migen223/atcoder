from math import *
a,b,d=map(int,input().split())

print(a*cos(radians(d))-b*sin(radians(d)),b*cos(radians(d))+a*sin(radians(d)))