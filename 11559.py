
while 1:
    try:
        participant, budget, hotelNumber, weekNumber = [int(x) for x in input().split()]
        rent = {}
        availableRooms = {}

        for i in range(hotelNumber):
            rent[i] = int(input())
            values = [int(x) for x in input().split()]
            for j in range(weekNumber):
                availableRooms[i, j] = values[j]

        minimumCost = -1

        for i in range(hotelNumber):
            for j in range(weekNumber):
                cost = participant * rent[i]
                if participant <= availableRooms[i, j] and cost <= budget:
                    if minimumCost == -1:
                        minimumCost = cost
                    elif cost < minimumCost:
                        minimumCost = cost

        if minimumCost == -1:
            print('stay home')
        else:
            print(minimumCost)
    except EOFError:
        break

