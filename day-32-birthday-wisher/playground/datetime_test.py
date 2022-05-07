import datetime as dt

week_day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Get current system date & time
now = dt.datetime.now()

# Access the current year
year = now.year
# Access the current month
month = now.month
# Access the current date
day = now.day
# Access the current day of the week; NOTE: Day 0 = Monday
day_of_week = now.weekday()
# Access current month, day, year, day of the week & its descriptive name
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Year: {year}")
print(f"Day of the week: {day_of_week}")
print(f"Today is: {week_day_name[day_of_week]}")
print("\n")

# Access details of a user-defined data
date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4, minute=30, second=45)
print(f"You're born on {date_of_birth}")
day_of_week = date_of_birth.weekday()
print(f"That was on {week_day_name[day_of_week]}")
