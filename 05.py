a = int(input("輸入三位數字 : "))
b = a//100
c = (a - (b *100)) //10
d = a % 10
e = (d * 100) + (c * 10) + b
print("結果 : " + str(e))