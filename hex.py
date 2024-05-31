import random as rdm


def hexRollsTrue(_=None):  # Seeker charm chance
    hexCount = 0
    for i in range(100_000):
        if rdm.randrange(10) == 0:  # Elite chance
            if rdm.randrange(1_500) == 0:  # Named chance
                hexCount += 1
            elif rdm.randrange(1_500) == 0:  # Elite hex chance
                hexCount += 1
        elif rdm.randrange(1_500_000) == 0:  # Normal Seeker
            hexCount += 1
    if hexCount != 0:
        bowsAverage = 100_000 / hexCount
    else:
        bowsAverage = 0
    values = [hexCount, True, bowsAverage]
    return values


def hexRollsFalse(_=None):  # No charm
    hexCount = 0
    for i in range(100_000):
        if rdm.randrange(50) == 0:  # Elite chance
            if rdm.randrange(1_500) == 0:  # Named chance
                hexCount += 1
            elif rdm.randrange(1_500) == 0:  # Elite hex chance
                hexCount += 1
        elif rdm.randrange(1_500_000) == 0:  # Normal Seeker
            hexCount += 1
    if hexCount != 0:
        bowsAverage = 100_000 / hexCount
    else:
        bowsAverage = 0
    values = [hexCount, False, bowsAverage]
    return values
