day_number_str = input ("If sunday was day 0 and saturday was day 6, on which number of day do you start your holiday")
day_number = int(day_number_str)

days_stayed_str = input ("how many nights do you plan to stay?")
days_stayed_int = int (days_stayed_str)                     
                     
final_day = (day_number + days_stayed_int) % 7                   
                     
print (final_day)

#this program asks someone to number the day that they are going on a holiday
#as sunday being day 0 and saturday being day 6, so monday would be 1
#tuesday 2, and so on. then it asks how many nights they are going to stay at the holiday
#then it finds the number of the day that the person will be back..

                        