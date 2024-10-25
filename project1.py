weight = input("Enter your weight: ")
unit_w = input("kg/lbs")
if unit_w == kg :
    conversion = int(weight)/0.45
else:
    conversion = int(weight) * 0.45

height = input("Enter your height: ")
unit_h = input("cm / ft")
if unit_h == cm:
    weight_conversion = 