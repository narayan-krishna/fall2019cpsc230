#program calculates number of chairs per building through user inputting chairs
#per classroom, classrooms per floor, and floor per building

def total_chairs():
  chairs_int = int(input("chairs per classroom: ")) #chairs per classroom
  classrooms_int = int(input("classrooms per floor: ")) #classrooms per floor
  floors_int = int(input("total floors: ")) #total floors in building

  total = chairs_int*classrooms_int*floors_int #calculation
  return("there are a total of " + str(total) + " chairs") #return

print(total_chairs())
