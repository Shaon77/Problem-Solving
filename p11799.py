def max_from_array(values=[]):
    if len(values) > 0:
        max_value = values[0]
        for x in values:
            if x > max_value:
                max_value = x
        return max_value


def main():
    caseCount = int(input())
    for i in range(caseCount):
        items = [int(x) for x in input().split()]
        items[0] = -1
        value = max_from_array(items)
        print('Case ' + str(i + 1) + ': ' + str(value))


if __name__ == "__main__":
    main()
