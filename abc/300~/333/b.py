s=input()
t=input()
dic={"AC":2,"AD":2,"AB":1,"AE":1,"BA":1,"BC":1,"BD":2,"BE":2,"CD":1,"CE":2,"CA":2,"CB":1,"DE":1,"DA":2,"DB":2,"DC":1,"EA":1,"EB":2,"EC":2,"ED":1}
if dic[s]==dic[t]:
    print("Yes")
else:
    print("No")