#Krishna Narayan
#2327205
#narayan@chapman.edu
#CPSC 230 section 08
#Assignment 1

def celsius():
    #takes user input of current temperature in celcius
    current_celsius = (input("input the current temperature in celcius: "))
    #does computatation
    current_fahrenheit = (float(current_celsius)*(float(9/5)) + 32)
    #returns value as a string for printing
    return str(current_fahrenheit)

print(celsius())
