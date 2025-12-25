# TO-DO import math
import math

while True:
  try:
    user_input = int(input('Enter a whole number (i.e., an integer): '))

    print(f'The number you entered is: {user_input}')
    if user_input % 2 == 0:
      print(f'{user_input} is an even number.')
    else:
      print(f'{user_input} is odd.')
# TO-DO Determine if number has perfect square root
    if user_input < 0:
      print('Cannot check for perfect square root of a negative number.')
    elif int(math.sqrt(user_input)) == math.sqrt(user_input):
      print(f'{user_input} has a perfect square root.')
    else:
      print(f'{user_input} does not have a perfect square root.')
# TO-DO Determine all factors of number
    if user_input > 0:
      factors = []
      for i in range(1, user_input + 1):
        if user_input % i == 0:
          factors.append(i)
      print(f'The factors of {user_input} are {factors}')

  except ValueError:
    print('Please enter a valid number.')

  again = input('Do you want to check another number? (y/n) ')
  if again != 'y':
    print('Thank you for playing!')
    break
