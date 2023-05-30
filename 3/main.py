def Correct(number):
    if((number / 100000) != 0): 
        if(Luck(number)): return True
    else: return False

def Luck(number):
    a = int(number / 100000) + int(number / 10000) % 10 + int(number / 1000) % 10
    b = int(number / 100) % 10 + int(number / 10) % 10 + int(number % 10)
    if(a == b): return True
    else: return False

number = int(input("Введите номер билета: "))
if(Correct(number)): print(str(number) + " ->  yes")
else: print(str(number) + " ->  no")