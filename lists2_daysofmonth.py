days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
##year = 2020
### use "%" to calculate the remainder from division
##if (year%4 == 0):
  ##  days_in_month[1] = 29


##Find the days in the year
num_days = 0
for i in range(12):
    num_days += days_in_month[i]
