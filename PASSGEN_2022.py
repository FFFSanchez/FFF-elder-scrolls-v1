from random import *

def generate_password(l, ch):
  password = ''
  for i in range(l):
    password += choice(ch)
  return password



dig = '0123456789'
low_let = 'abcdefghijklmnopqrstuvwxyz'
hi_let = low_let.upper()
puncts = '!#$%&*+-=?@^_'
bads = 'il1Lo0O'

chrs = ''

amnt = int(input('how much pass to gen? '))
leng = int(input('pass length: '))
if input('use digits?: y/n') == 'y':
  chrs += dig

if input('use upper lets?: y/n') == 'y':
  chrs += hi_let

if input('use lower lets?: y/n') == 'y':
  chrs += low_let

if input('use puncts?: y/n') == 'y':
  chrs += puncts

if input('exclude bad symbls?: y/n') == 'n':
  chrs += bads

for i in range(amnt):
  print(generate_password(leng, chrs))