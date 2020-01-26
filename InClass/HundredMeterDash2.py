def hundred_meter_dash():
    time = float(input("input hundred meter dash time: "))
    miles_per_hour = meters_to_miles(100) / seconds_to_hours(time)
    print("you're running around " + str(int(miles_per_hour)) +
    " miles per hour")

def meters_to_miles(meters):
    feet = 3.28 * meters
    miles = feet/5280
    return miles

def seconds_to_hours(seconds):
    minutes = seconds/60
    hours = minutes/60
    return hours

hundred_meter_dash()
