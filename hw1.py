a = int(input('Введите  номер билета: '))
while a < 100000 or a > 999999:
    a = int(input('Неверно! Номер билета - шестизначное число! Введите  номер билета: '))
firstNumber = a//100000
secondNumber = a // 10000 % 10
thirdNumber = a//1000 % 10
fourthNumber = a//100 % 10
fifthNumber = a//10 % 10
sixthNumber = a % 10
if firstNumber+secondNumber+thirdNumber == fourthNumber+fifthNumber+sixthNumber:
    print('yes')
else:
    print('no')
