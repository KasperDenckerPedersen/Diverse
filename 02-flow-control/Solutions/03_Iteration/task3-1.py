'''
Adapt the code to get user input into the number variable. Change the print statement so it outputs 'number' multiplied by 'counter' equal 'product'. 
Make the counter increase by 2 every loop. Add a line once the loop has finished to output 'The loop has finished'
'''

number = int(input('Number: '))
counter = 1

while counter < 11:
    product = counter * number
    print(f'{number} x {counter} = {product}')
    counter += 2

print('The loop has finished')