
while 1:
    items = [x for x in input().split()]
    duration = int(items[0])
    if duration < 0:
        break
    else:
        downPayment = float(items[1])
        loanAmount = float(items[2])
        depriciationNumber = int(items[3])

        depValues = {}

        for i in range(depriciationNumber):
            values = [x for x in input().split()]
            depValues[int(values[0])] = float(values[1])

        carCurrentValue = (loanAmount + downPayment) * (1 - depValues[0])
        loanOwed = loanAmount
        monthlyPayment = loanAmount / duration

        selectedMonth = 1;
        selectedDepriciation = depValues[0]

        if carCurrentValue > loanOwed:
            selectedMonth = 0

        while selectedMonth > 0:
            if selectedMonth in depValues:
                selectedDepriciation = depValues[selectedMonth]

            loanOwed = loanOwed - monthlyPayment
            carCurrentValue = carCurrentValue * (1 - selectedDepriciation)

            if carCurrentValue > loanOwed:
                break

            selectedMonth = selectedMonth + 1
        if selectedMonth == 1:
            print(str(selectedMonth) + ' month')
        else:
            print(str(selectedMonth) + ' months')



