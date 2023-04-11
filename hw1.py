a = int(input('Введите трехзначное чило: '))
while (a < 100 or a > 999):
    a = int(input('Неверно! Введите трехзначное чило: '))
firstNumber = a//100
secondNumber = a//10 % 10
thirdNumber = a % 100 % 10
print(firstNumber+secondNumber+thirdNumber,
      '(', firstNumber, '+', secondNumber, '+', thirdNumber, ')')
