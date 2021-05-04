from time_calculator import add_time

if __name__ == '__main__':
    d = add_time('3:00 PM', '3:10')
    print(d)  # 6:10 PM

    d = add_time('11:30 AM', '2:32', 'Monday')
    print(d)  # 2:02 PM, Monday

    d = add_time('11:43 AM', '00:20')
    print(d)  # 12:03 PM

    d = add_time('10:10 PM', '3:30')
    print(d)  # 1:40 AM (next day)

    d = add_time('11:43 PM', '24:20', 'tueSday')
    print(d)  # 12:03 AM, Thursday (2 days later)

    d = add_time('6:30 PM', '205:12')
    print(d)  # 7:42 AM (9 days later)
