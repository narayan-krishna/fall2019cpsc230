#Krishna Narayan
#2327205
#narayan@chapman.edu
#CPSC 230 section 08
#Assignment 1

#calculate the area of a triangle

def triangle ():
    base = int(input("input base length: ")) #input
    height = int(input("input height length: ")) #input
    area = (base*height)*(1/2) #calculation
    return area #return product

print(str(triangle()) + " square meters")
