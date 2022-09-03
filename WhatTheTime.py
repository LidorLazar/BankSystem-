from datetime import datetime


def get_time(user_input):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    hour_clock = str(current_time).split(':')[0]
    minutes_clock = str(current_time).split(':')[1]
    seconds_clock = str(current_time).split(':')[2]
    user_hour = user_input.split(":")[0]
    user_minutes = user_input.split(":")[1]
    user_seconds = user_input.split(":")[2]
    difference_hour = int(hour_clock) - int(user_hour)
    difference_minutes = int(minutes_clock) - int(user_minutes)
    difference_seconds = int(seconds_clock) - int(user_seconds)
    return f'The hour difference is {difference_hour} the minutes difference is {difference_minutes} ' \
           f'the seconds difference is {difference_seconds} '


print(get_time('9:10:00'))