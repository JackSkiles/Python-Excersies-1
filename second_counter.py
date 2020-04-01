day = 24

number_of_days = input('Please input number of days ' )

hours = int(number_of_days) * day

seconds_in_day = hours * 3600

print('There are ' + str(seconds_in_day) + ' seconds in ' + number_of_days + ' days')