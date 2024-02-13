year = 100

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print (year,"is Leap year")
else:
    print(year,"is not leap year")