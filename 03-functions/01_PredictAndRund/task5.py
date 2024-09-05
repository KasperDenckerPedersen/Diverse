# Add comments to this code to explain how it works and predict what it will do.
import sys
import time

sys.setrecursionlimit(10**6)

def sum(number):
    if number > 0:
        return number + sum(number - 1)
    return 0

def smart_sum(number):
    return number * (number + 1) / 2

startTime = time.time()
result = sum(10000)
endTime = time.time()
diffTime = endTime - startTime
print(f'The result is {result}. It took {diffTime} seconds')

startTime = time.time()
result = smart_sum(10000)
endTime = time.time()
diffTime = endTime - startTime
print(f'The result is {result}. It took {diffTime} seconds')
