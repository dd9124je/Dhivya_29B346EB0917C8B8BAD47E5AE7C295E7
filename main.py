input_year = int(input("enter a year: "))
def is_leap(year):
  if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    return True

    return False
if is_leap(input_year):
  print(" It is a leap year")
else:
  print(" It is not a leap year")
