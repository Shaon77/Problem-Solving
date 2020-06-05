
while 1:
    caseCount = int(input())
    if caseCount == 0:
        break
    else:
        divX, divY = [int(x) for x in input().split()]
        for i in range(caseCount):
            resX, resY = [int(x) for x in input().split()]
            if resY == divY or resX == divX:
                print('divisa')
            elif resY > divY:
                if resX > divX:
                    print('NE')
                else:
                    print('NO')
            else:
                if resX > divX:
                    print('SE')
                else:
                    print('SO')
