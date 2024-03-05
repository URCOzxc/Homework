#import time function perf_counter_ns which counts in nanno secs
from time import perf_counter_ns

#asks for name
print(end="please enter your name: ")

#creates function start_time and sets it = to the time function
start_time = perf_counter_ns()

#sets function name = to user input
name = input()

#creates 
stop_time = perf_counter_ns()

#creates function elapsed and sets = to StopT minus startT devided by 1 billion
elapsed = stop_time - start_time/1_000_000_000

#prints user imputed name and the time it took to respond
print(f"Hello, {name}, you took {elapsed} seconds to respond.")


#code that will help with lab
# import math
#     from random import randrange
#gives a sudo random number between 10 and 21
#print(randrange(10, 21))