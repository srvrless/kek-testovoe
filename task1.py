from datetime import datetime


def days_and_seconds_between_dates(start_date, end_date):
    start = datetime(*start_date)
    end = datetime(*end_date)
    difference = end - start
    total_seconds = difference.total_seconds()
    days = difference.days
    seconds = total_seconds - days * 24 * 3600
    return days, int(seconds)


start_date = list(map(int, input().split()))
end_date = list(map(int, input().split()))

days, seconds = days_and_seconds_between_dates(start_date, end_date)

print(days, seconds)
# ящеры оказались сильнее этого задания