def leap(year) -> bool:
    leap_year = False

    if year % 4 == 0:
        leap_year = True
    if year % 100 == 0 and year % 400 != 0:
        leap_year = False

    return leap_year
