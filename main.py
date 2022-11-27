import random

global lives
lives = 10

min = 1
max = 100

global ans
ans = random.randint(min,max)

def new():
  global num
  global lives
  print(f'CHANCES LEFT = {lives} ❤️')
  num = int(input(f'TRY TO GUESS THE NUMBER BETWEEN - ({min} to {100}) \n=>\t'))
  check()

def get():
  global num
  global lives
  lives-=1
  print(f'CHANCES LEFT = {lives} 💔')
  if lives<=0:
    print(f'\n\n👎GAME OVER👎\nTHE NUM WAS => {ans}')
    return
  num = int(input('=>\t'))
  check()

def check():
  global num
  global ans
  if num>ans:
    print('⬇️⬇️⬇️ TRY LOWER ⬇️⬇️⬇️')
    get()
  elif num<ans:
    print('⬆️⬆️⬆️ TRY HIGHER ⬆️⬆️⬆️')
    get()
  elif num==ans:
    print(f'🎉YOU GUESSED IT CORRECT🎉\nTHE NUM IS =>\t{ans}')

new()