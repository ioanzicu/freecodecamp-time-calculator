from datetime import datetime, timedelta
import calendar


def add_time(start, duration, week_day=''):

    try:
        start_format_str = '%I:%M %p'  # %I - 12 hours format;  %H - 24 hours format
        start_time = datetime.strptime(start, start_format_str)

        duration_hour, duration_minutes = duration.split(':')

        duration_hour = int(duration_hour)
        duration_minutes = int(duration_minutes)

        duration_delta = timedelta(
            hours=duration_hour, minutes=duration_minutes)

        final_time = start_time + duration_delta

        # %#I (Windows) | %-I (Unix) - will remove 0 when hour is < 10
        final_format_str = '%#I:%M %p'
        final_time_str = final_time.strftime(final_format_str)

        days_diff = final_time.day - start_time.day

        days_of_week = list(calendar.day_name)
        if week_day:
            start_day_index = 0
            for index, day in enumerate(days_of_week):
                if week_day.capitalize() == day:
                    start_day_index = index
                    break

            final_weekday_index = (
                start_day_index + days_diff) % 7  # days of week
            final_time_weekday = days_of_week[final_weekday_index]
            final_time_str += f', {final_time_weekday}'

        # print(final_time.weekday())
        if days_diff == 1:
            final_time_str += ' (next day)'
        elif days_diff > 1:
            final_time_str += f' ({days_diff} days later)'

        return final_time_str

    except Exception as err:
        print(err)
        exit()


if __name__ == '__main__':
    d = add_time("3:00 PM", "3:10")
    print(d)
    d = add_time("11:30 AM", "2:32", "Monday")
    print(d)
    d = add_time("11:43 AM", "00:20")
    print(d)
    d = add_time("10:10 PM", "3:30")
    print(d)
    d = add_time("11:43 PM", "24:20", "tueSday")
    print(d)
    d = add_time("6:30 PM", "205:12")
    print(d)
