
print(f'please enter non-negative numbers (-1 ends list)')
sum = 0
done = False  #also would work if looping = True
while not done:

    entry = float(input('=> '))
    if entry >0.0:
        sum += entry
    else:
        done = True # and also looping = False
print(f"the sum is{sum}")