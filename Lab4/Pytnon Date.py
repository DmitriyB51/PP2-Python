# ex 1

from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)
a = new_date.strftime('%Y-%m-%d')
# print(a)

# ex 2
today = datetime.now()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)


formatted_dates = f"Yesterday: {yesterday.strftime('%Y-%m-%d')}\nToday: {today.strftime('%Y-%m-%d')}\nTomorrow: {tomorrow.strftime('%Y-%m-%d')}"
# print(formatted_dates)

# ex 3

date_with_microsec = datetime.now()
date_without_microsec = date_with_microsec.replace(microsecond=0)

# print(date_without_microsec)

# ex 4

date1 = datetime(2024, 2, 1, 12, 0, 0)
date2 = datetime(2024, 2, 3, 12, 0, 0)
difference = (date2 - date1).total_seconds()

print(difference)

