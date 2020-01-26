percentage = float(input("input grade: "))
while (percentage > 100):
    print("grade cannot be over 100")
    percentage = float(input("input grade: "))
if percentage >= 70:
    print("congrats, you passed")
    if percentage >= 90:
        print("you got an A")
    if percentage >= 80 and percentage < 90:
        print("you got a B")
    if percentage >= 70 and percentage < 80:
        print("you got a C")
elif percentage >= 60:
    print("you got a D")
else:
    print ("you got an F")

print("happy holidays")
