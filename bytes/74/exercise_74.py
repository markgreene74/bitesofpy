from calendar import weekday, day_name


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    return day_name[date.weekday()]
