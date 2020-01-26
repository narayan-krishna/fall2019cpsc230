#Krishna Narayan
#2327205
#narayan@chapman.edu
#CPSC 230 section 08
#Assignment 1

#calculating total hours, minutes and seconds based on total amount of seconds
def seconds():
    #takes input
    total_seconds = int(input("input total amount of seconds "))
    #divides out hours
    exact_hours = total_seconds / 3600
    #defines remaining seconds
    remaining_seconds = total_seconds % 3600
    #divides out minutes
    exact_minutes = remaining_seconds / 60
    #takes remainder as final remaining seconds
    exact_seconds_final = (remaining_seconds % 60)
    #prints with rounding for readability.
    return str(int(exact_hours)) + " hours, " + str(int(exact_minutes)) + " minutes, " + str(int(exact_seconds_final)) + " seconds "

print(seconds())
