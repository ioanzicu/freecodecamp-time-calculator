from datetime import datetime, timedelta
import calendar


def get_weekday(week_day, days_diff) -> str:
    '''Returns weekday index.'''
    days_of_week = list(calendar.day_name)
    start_day_index = 0
    for index, day in enumerate(days_of_week):
        if week_day.capitalize() == day:
            start_day_index = index
            break

    final_weekday_index = (
        start_day_index + days_diff) % 7  # days of week
    weekday = days_of_week[final_weekday_index]

    return weekday


def get_duration_delta(duration) -> timedelta:
    '''Returns a timedelta object with specified time in the duration parameter.'''
    try:
        duration_hour, duration_minutes = duration.split(':')
        duration_hour = int(duration_hour)
        duration_minutes = int(duration_minutes)

        return timedelta(
            hours=duration_hour, minutes=duration_minutes)
    except Exception as err:
        print(err)
        exit()


def add_time(start, duration, week_day='') -> str:
    try:
        start_format_str = '%I:%M %p'  # %I - 12 hours format;  %H - 24 hours format
        start_time = datetime.strptime(start, start_format_str)

        duration_delta = get_duration_delta(duration)
        final_time = start_time + duration_delta

        # %#I (Windows) | %-I (Unix) - remove 0 when hour is < 10
        final_format_str = '%#I:%M %p'
        final_time_str = final_time.strftime(final_format_str)

        days_diff = final_time.day - start_time.day

        if week_day:
            final_weekday = get_weekday(week_day, days_diff)
            final_time_str += f', {final_weekday}'

        if days_diff == 1:
            final_time_str += ' (next day)'
        elif days_diff > 1:
            final_time_str += f' ({days_diff} days later)'

        return final_time_str

    except Exception as err:
        print(err)
        exit()
