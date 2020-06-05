

caseCount = int(input())

for i in range(caseCount):
    firstNumber, secondNumber = [int(x) for x in input().split()]
    if firstNumber > secondNumber:
        print('>')
    elif firstNumber < secondNumber:
        print('<')
    else:
        print('=')
