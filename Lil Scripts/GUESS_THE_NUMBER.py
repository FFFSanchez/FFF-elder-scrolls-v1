from random import *

def is_valid(p):
  #p = int(p)
  if p.isdigit() and 0 < int(p) < rb:
    return True
  else:
    return False

def nr(rb):
  return randint(1, rb)

print('Welcome to the game GUESS THE NUMBER')
print('Try to guess number in range from 1 to n')

def game(n):
  t = 0
  while True:
    p = input('your purpose: ')
    if is_valid(p):
      t += 1
      p = int(p)
      if p == n:
        print('Bingo!')
        print(f'It took {t} tries')
        break
      else:
        print('No, try again')
        if p < n:
          print('your number < than answer')
        elif p > n:
          print('your number > than answer')
    else:
      print(f'only numbers 1 - {rb} is valid')


while True:
  rb = int(input('enter the right border n: 1 - '))
  game(nr(rb))
  if input('again? type "y" or press any to exit ') == 'y':
    continue
  else:
    print('well, bye')
    break