
def minFromArray(list = []):
    if len(list) > 0:
        min = list[0]
        for x in list:
            if x < min:
                min = x
        return min

def maxFromArray(list = []):
    if len(list) > 0:
        max = list[0]
        for x in list:
            if x > max:
                max = x
        return max

def sumFromArray(list = []):
    sum = 0
    for x in list:
        sum = sum + x
    return sum


def main():
    caseCount = int(input())
    for i in range(caseCount):
        items = [int(x) for x in input().split()]
        second = sum(items) - minFromArray(items) - maxFromArray(items)
        print('Case ' + str(i + 1) + ': ' + str(second))


if __name__ == "__main__":
    main()
