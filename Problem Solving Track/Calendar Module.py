"""The calender.day_name returns an array of names in a week as set by locale.
This approach will not work if we manually set the first day of the week anything
apart from a monday as currently we are doing it based on the index value.The if elif
approach would also need to be changed in that case."""

import calendar

month, day, year = map(int, input().split())

day_of_week = calendar.weekday(year, month, day)

# print(list(calendar.day_name))
print(calendar.day_name[day_of_week].upper())

# if day_of_week==0:
#     print("MONDAY")

# elif day_of_week==1:
#     print("TUESDAY")

# elif day_of_week==2:
#     print("WEDNESDAY")

# elif day_of_week==3:
#     print("THURSDAY")

# elif day_of_week==4:
#     print("FRIDAY")

# elif day_of_week==5:
#     print("SATURDAY")

# else:
#     print("SUNDAY")
