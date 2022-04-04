i = 0
last_dig = 0
while i <= 100:
    if 2 <= i < 5:
        print(i, " процента")
    elif i == 1:
        print(i, " процент")
    elif 5<= i <= 20 or i == 100:
        print(i, " процентов")
    elif 21 <= i < 100:
        last_dig = i % 10
        if 2 <= last_dig < 5:
            print(i, " процента")
        elif last_dig == 1:
            print(i, " процент")
        elif 5 <= last_dig <= 9 or last_dig == 0:
            print(i, " процентов")
    i+=1