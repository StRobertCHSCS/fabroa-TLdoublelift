name = "Razwog" or "JoeMama"
input_name = input("Enter your name: ")

has_reservation = name == input_name

if has_reservation:
    print("Right this way please!")

else:
    print("Sorry, we do not ave a reservation in this name.")