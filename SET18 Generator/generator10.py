# Write a generator that generates a sequence of dates within a specific range.

from datetime import datetime, timedelta

# Define the generator to yield dates in a specific range
def date_range_generator(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)

# Example usage
start = datetime(2023, 9, 1)
end = datetime(2023, 9, 5)

# Generate the dates
dates = date_range_generator(start, end)

# Iterate through the generator and print each date
for date in dates:
    print(date.strftime("%Y-%m-%d"))



'''
2023-09-01
2023-09-02
2023-09-03
2023-09-04
2023-09-05

'''