a = int(input("請輸入一個十進制數字 : "))
b = bin(a)
c = oct(a)
d = hex(a)
print("二進制 :" +  "{:b}" .format(a, "b") )
print("八進制 :" +  "{:o}" .format(a, "o") )
print("十六進制 :" +  "{:x}" .format(a, "x") )