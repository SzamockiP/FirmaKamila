def ustalPremie (wynagrodzenie:float):
    if (wynagrodzenie < 10000):
        return 0.10
    elif (wynagrodzenie >= 10000 and wynagrodzenie < 15000):
        return 0.12
    elif (wynagrodzenie >= 15000 and wynagrodzenie < 18000):
        return 0.14
    elif (wynagrodzenie >= 18000 and wynagrodzenie < 22000):
        return 0.10
    elif (wynagrodzenie >= 22000):
        return 0.2