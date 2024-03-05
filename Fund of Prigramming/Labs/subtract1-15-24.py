



#print("Twenty dollar bills:",twenty)
#print("Ten dollar bills:",tens)
#print("Five dollar bills:",fives)
#print("One dollar bills:",ones)
#print("Quarters:",quarters)
#print("Dimes:",dimes)
#print("Nickels:",nickles)
#print("Pennies:",pennies)



#total_cash = twenty * 20 + tens * 10 + fives * 5 + ones * 1 + quarters * .25 + nickles * .05 + dimes * .10 + pennies * .01 

#print(f'total cash is {total_cash:,}')
#money = int(float(input('Please enter a money amount (No dollar sign. Example 20.56):')))

"""twenties = int(input("Twenty dollar bills:"))
tens = int(input("Ten dollar bills:"))
fives = int(input("Five dollar bills:"))
ones = int(input("One dollar bills:"))
quarters = int(input("Quarters:"))
dimes = int(input("Dimes:"))
nickels = int(input("Nickels:"))
pennies = int(input("Pennies:"))"""

#totalCents = (twenties * 2000) + (tens * 1000) + (fives * 500) + (ones * 100) + (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies

"""total_cents = int(100 * all_the_money)
print(total_cents)
twenty = int(2000 // all_the_money)
tens = int(1000 // all_the_money)
fives = int(500 // all_the_money)
ones = int(100 // all_the_money)
quarters = int(25 // all_the_money)
dimes = int(10 // all_the_money)
nickles = int(5 // all_the_money)"""

total_money = input('Please enter total amount of money (no dollar sign example 20.48):')

all_the_money = float(total_money)

total_cents = int(round(100 * all_the_money))

twenties = total_cents // 2000
total_cents %= 2000

tens = total_cents // 1000
total_cents %= 1000

fives = total_cents // 500
total_cents %= 500

ones = total_cents // 100
total_cents %= 100

quarters = total_cents // 25
total_cents %= 25

dimes = total_cents // 10
total_cents %= 10

nickels = total_cents // 5
total_cents %= 5

pennies = total_cents

print("Twenty dollar bills:", twenties)
print("Ten dollar bills:", tens)
print("Five dollar bills:", fives)
print("One dollar bills:", ones)
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
