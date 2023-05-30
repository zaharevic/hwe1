def rectangle(quantity,m,n):
    if((quantity % n) == 0 or (quantity % m) == 0): return True
    else: return False



m = int(input("Введите m: "))
n = int(input("Введите n: "))
quantity = int(input("Введите количество долек:"))
if(rectangle(quantity, m,n)): print(str(m)+ " "+ str(n) +" "+ str(quantity) + " ->  yes")
else: print(str(m)+ " "+ str(n) +" "+ str(quantity) + " ->  no")