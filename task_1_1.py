duration = int(input('Введите длительность в секундах: '))
if duration < 60:
    print(duration, ' сек')
elif 60 <= duration < 3600:
    minuts = duration // 60
    sec = duration % 60
    print(minuts, ' мин ', sec, ' сек ')
elif 3600 <= duration < 86400:
    hours = duration // 3600
    minuts = duration % 3600 // 60
    sec = duration % 3600 % 60
    print(hours, 'час', minuts, ' мин ', sec, ' сек ')
elif 86400 <= duration:
    days = duration // 86400
    hours = duration % 86400 // 3600
    minuts = duration % 86400 % 3600 // 60
    sec = duration % 86400 % 3600 % 60
    print(days, ' дн ', hours, 'час', minuts, ' мин ', sec, ' сек ')
