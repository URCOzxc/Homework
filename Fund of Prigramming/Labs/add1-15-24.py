#first try

"""
twenty = int(input('Please enter number of twenty dollar bills:'))
tens = int(input('Please enter number of ten dollar bills:'))
fives = int(input('Please enter number of five dollar bills:'))
ones = int(input('Please enter number of one dollar bills:'))
quarters = int(input('Please enter number of quarters:'))
nickles = int(input('Please enter number of nickles:'))
dimes = int(input('Please enter number of dimes:'))
pennies = int(input('Please enter number of pennies:'))


print("Twenty dollar bills:",twenty)
print("Ten dollar bills:",tens)
print("Five dollar bills:",fives)
print("One dollar bills:",ones)
print("Quarters:",quarters)
print("Dimes:",dimes)
print("Nickels:",nickles)
print("Pennies:",pennies)



total_cash = twenty * 20 + tens * 10 + fives * 5 + ones * 1 + quarters * .25 + nickles * .05 + dimes * .10 + pennies * .01 

print(f'total cash is {total_cash:,}')
"""

#second try


#assigns user input to equal money var names.
twenties = int(input("Please enter the number of twenty dollar bills:"))
tens = int(input("Please enter the number of ten dollar bills:"))
fives = int(input("Please enter the number of five dollar bills:"))
ones = int(input("Please enter the number of one dollar bills:"))
quarters = int(input("Please enter the number of quarters:"))
dimes = int(input("Please enter the number of dimes:"))
nickels = int(input("Please enter the number of nickels:"))
pennies = int(input("Please enter the number of pennies:"))

#multiplies money var names by the cent value and adds them all together.
totalCents = (twenties * 2000) + (tens * 1000) + (fives * 500) + (ones * 100) + (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies

#prints the total amount of cents in $ dollar format (ie $2.48).
print(f'Total cash: ${totalCents//100}.{totalCents%100:02}')
#x = (b2 - b1) / (m1 - m2)
    #y = (m1 * x) + b1
    # i_x = i_y = inf