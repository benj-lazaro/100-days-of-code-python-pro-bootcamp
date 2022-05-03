import datetime as dt

# Get current system date & time
now = dt.datetime.now()

# Access the current year
year = now.year
# Access the current month
month = now.month
# Access the current day of the week; NOTE: Day 0 = Monday
day_of_week = now.weekday()

print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day of the week: {day_of_week}")

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)
