def Correct(number):
    if ((number%6)== 0 ): return True
    else: return False

number = int(input("Введите колиество жупавлей: "))
if(Correct(number)): print(str(number) + " -> " + str(int(number/6)) + " " + str(int(number/3)) + " " + str(int(number/ 6)))
else: print("Неверное число!") 