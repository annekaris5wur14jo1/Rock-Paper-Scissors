# A = 0
# B = 10
# greeting = "hello"
# if (A < B):
#     print(greeting)
# else:
#     print("A is greater than B")

lamp = input("Is the lamp plugged in? (yes/no)")
lamp = lamp.lower()
light = input("Is the light turned on? (yes/no)")

if (lamp ==  "no" and light == "no"):
    print("Plug in the lamp")
elif(lamp == "yes" and light == "no"):
    print("Bulb is burnt, change the bulb")
    light = input("Is the light turned on? (yes/no)")
    light = light.lower()
else:
    print("Buy new lamp")

    