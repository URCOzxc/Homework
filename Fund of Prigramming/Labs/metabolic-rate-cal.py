sex = input('Please enter your biological sex (female or male): ').lower()


if sex == "male" or sex == "female":
    weight = int(input('Please enter your weight in pounds: '))
    height = input('Please enter your height in feet and inches separated by a space: ')
    age = int(input('Please enter your age in years: '))
    print('Activity levels:')
    print('1 sedentary')
    print('2 somewhat active (exercise occasionally)')
    print('3 active (exercise 3 or 4 days a week)')
    print('4 highly active (exercise everyday)')
    level = input('Please enter your activity level (1, 2, 3, or 4): ')
    if int(level) < 1 or int(level) > 4:
        print("Activity level must be one of 1, 2, 3, or 4; please rerun the program.")
        quit()

    w = (weight * 0.453529)
    h = height 
    first_ft = int(h.split()[0])
    second_in = int(h.split()[1])
    total_inches = first_ft * 12 + second_in
    total_centimeters = (total_inches * 2.54)

    if sex == "male":
        bmr = (w * 10) + (total_centimeters * 6.25) - (age * 5) + 5

    elif sex == "female":
        bmr = (w * 10) + (total_centimeters * 6.25) - (age * 5) - 161

        

    # example 100+(100*0.2  for 20)
        
    if level == "1":
        total_calories = (bmr * 1.2)
        #calories = (bmr / 20) 
        #total_calories = (calories * 1.2)
    if level == "2":
        total_calories = (bmr * 1.3)
        #calories = (bmr / 30) 
        #total_calories = (calories * 1.3)  

    if level == "3":
        total_calories = (bmr * 1.4)
        #calories = (bmr / 40) 
        #total_calories = (calories * 1.4)

    if level == "4":
        total_calories = (bmr * 1.5)
        #calories = (bmr / 50) 
        #total_calories = (calories * 1.5)

    bread = total_calories / 69
        

    print(f'Total energy required per day is {total_calories:.1f} kcals.')
    print(f'To maintain your weight, you must consume the equivalent of {bread:.1f} slices of whole wheat bread per day.')

    
else:
    print("Gender is not recognized; please rerun the program")
    quit()