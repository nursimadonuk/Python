string_seconds = input("Enter the number of secondds ou wish to convert,")
entered_int_seconds = int(string_seconds)

#this prongram converts the entered number of seconds
#to hours minutes and seconds

hours = entered_int_seconds // 3600
seconds_left = entered_int_seconds % 3600
minutes= seconds_left // 60
final_seconds = seconds_left % 60
print (entered_int_seconds, "seconds is equal to", hours, "hours", minutes, "minutes and", final_seconds, "seconds.")
