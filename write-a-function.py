#Checking if a year is a leap year or not
def is_leap(year):
    leap = False
    
    leftover4 = year % 4
    leftover100 = year % 100
    leftover400 = year % 400
    if leftover4 == 0:
        leap = True
        if leftover100 == 0:
            leap = False
        if leftover400 == 0:
            leap = True
    else:
        leap = False
    return leap

year = int(input())
