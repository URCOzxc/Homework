user_number = int(input("Please enter number from 1 to 10#: "))

if user_number <= 4:
    print("number is too low")
else:
    if user_number >= 6:
        print("number is too high")
    else:
        if user_number == 5:
            print("number is just right")
