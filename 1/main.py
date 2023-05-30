number = int(input("Введите число: "))
print(str(number) + " -> " + str((int((number/100)))+ (int((number  % 100 / 10)))+ (number % 10)))