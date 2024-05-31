import random as rdm


def hexRollsTrue():  # Seeker charm chance
    hexCount = 0
    for i in range(100000):
        if rdm.randint(0, 9) == 0:  # Elite chance
            if rdm.randint(0, 1499) == 0:  # Named chance
                hexCount += 1
            else:  # Elite hex chance
                if rdm.randint(0, 1499) == 0:
                    hexCount += 1
        else:  # Normal Seeker
            if rdm.randint(0, 1499999) == 0:
                hexCount += 1
    if hexCount != 0:
        bowsAverage = 100000 / hexCount
    else:
        bowsAverage = 0
    values = [hexCount, "True", bowsAverage]
    return values


def hexRollsFalse():  # No charm
    hexCount = 0
    for i in range(100000):
        if rdm.randint(0, 49) == 0:  # Elite chance
            if rdm.randint(0, 1499) == 0:  # Named chance
                hexCount += 1
            else:  # Elite hex chance
                if rdm.randint(0, 1499) == 0:
                    hexCount += 1
        else:  # Normal Seeker
            if rdm.randint(0, 1499999) == 0:
                hexCount += 1
    if hexCount != 0:
        bowsAverage = 100000 / hexCount
    else:
        bowsAverage = 0
    values = [hexCount, "False", bowsAverage]
    return values
