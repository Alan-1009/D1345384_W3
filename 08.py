a = int(input("請輸入一個五位數 : "))
b = a//10000
c = (a - (b*10000))//1000
d = (a - (b*10000) -(c*1000) )//100
e = (a - (b*10000) - (c*1000) - (d*100))//10
f = (a - (b*10000) - (c*1000) - (d*100) - (e*10))
print("結果 :")
print(str(b))
print(str(c))
print(str(d))
print(str(e))
print(str(f))