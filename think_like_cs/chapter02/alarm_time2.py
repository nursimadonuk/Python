time_right_now_string = input ("what time is it now (in hours), in the 24 hour clock?")
time_int = int(time_right_now_string)
hours_for_alarm_string = input ("how many hous later should the alarm go off?")
alarm_hours_int = int(hours_for_alarm_string)
hours = alarm_hours_int % 24
alarm_time = hours + time_int
if alarm_time < 24 :
    print (alarm_time)
else:
    print (alarm_time - 24)
