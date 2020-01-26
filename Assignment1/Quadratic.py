#Krishna Narayan
#2327205
#narayan@chapman.edu
#CPSC 230 section 08
#Assignment 1

import math

def quadratic():
    #takes user input of three coefficients
    coeff_a = float(input("input first coefficient "))
    coeff_b = float(input("input second coefficient "))
    coeff_c = float(input("input third coefficient "))

    #establish discriminant and divisor so end computatation is more readable
    discriminant = (coeff_b*coeff_b) - (4*coeff_a*coeff_c)
    if discriminant >= 0:
        divisor = 2*coeff_a

        plus_dividend = ((0-coeff_b) + math.sqrt(discriminant)) #calculate + dividend
        plus_root = (plus_dividend/divisor) #plus root
        minus_dividend = ((0-coeff_b) - math.sqrt(discriminant)) #calculate - dividend
        minus_root = (minus_dividend/divisor) #minus root
        return("your roots are " + str(plus_root) + " and " + str(minus_root) + ".")
    else:
        return("discriminant is negative")

print(quadratic())
