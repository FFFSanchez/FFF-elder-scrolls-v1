from random import *

ans = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай", "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Hi, I am the one who say the truth')
name = input('What is your name?: ')
print(f'Hi, {name}')

def go():
  input('Write your question: ')
  print(choice(ans))

while True:
  go()
  f = input('more questions?: y/n ')
  if f == 'y':
    continue
  else:
    print('go your own way, bye')
    break