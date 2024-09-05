# Add comments to this code to explain how it works and predict what it will do.
import sys # Import sys library
import time # Import time library
import numpy as np

sys.setrecursionlimit(10**6) # Set the recursion limit (you can ignore this - it is just a technicality)

def sum(number): # Define a recursive function to calculate the sum of all integers from 1 up to the value number. This function will keep calling itself until number is 0
    if number > 0:
        return number + sum(number - 1)
    return 0

def smart_sum(number): # Define a function to calculate the sum of all integers from 1 up to the value number in a more efficient way using the Gauss sum
    return number * (number + 1) / 2

startTime = time.time() # Time at the moment line 15 is run
result = sum(10000) # Use recursive sum formula to get sum of all integers from 1 to 10000
endTime = time.time() # Time at the moment line 17 is run
diffTime1 = endTime - startTime # Difference in times to check how long it took to calculate the sum using the recursive function
print(f'The result is {result}. It took {diffTime1} seconds')

startTime = time.time() # Time at the moment line 21 is run
result = smart_sum(10000) # Use Gauss sum formula to get sum of all integers from 1 to 10000
endTime = time.time() # Time at the moment line 23 is run
diffTime2 = endTime - startTime # Difference in times to check how long it took to calculate the sum using the Gauss sum formula
print(f'The result is {result}. It took {diffTime2} seconds')

print(f'The smart sum is {round(diffTime1/diffTime2)}-times as fast as the normal sum') # Compare the speed of both functions
