import json
import re
from random import choice

def read_base(filename):

  try:
    with open(base, 'r' , encoding='utf-8') as f:
      return json.load(f)
  except:
    print('Error to open')
    raise


"""
check guessed or not
"""
def check_it(secret, sym):

  if re.findall(sym, secret):
    for m in re.finditer(sym, secret):
      show_secret(m.span(),m.group())
    return 'Found:' + sym
  else:
    print()
    return 'Oops. Try again'


"""
show guessed positions
if not have args - show all word as asterisks
"""
def show_secret(pos, find):

  if pos and find:
    # global var!
    guessed[pos[0]] = find
  # show what user guested
  for s in guessed:
    # print without newline
    print(s,end='')
  print()

"""
get 1 symbol from user , if more than 1 symbol - iterate
"""
def get_sym():
  try:
    answer = input("Enter 1 symbol:")
    #if answer == 'quit':
    #  exit;
    assert len(answer) == 1
  except:
    print('Only 1 symbol accept')
    get_sym()

  return answer

"""
check for guessed all symbols in the word
"""
def check_result():
  if '*' in guessed:
    return 1
  else:
    print('Congratulation, you are win! Result:[ ' + ''.join(guessed) + ' ]')
    return 0


version = '1.0'
author = 'pavel kuptsov'

base = 'words.txt'
db_data = read_base(base)
# get first key from dict
secret = ( next( iter(db_data) ) )
# make a tulpe * depend from length of word
guessed = list(len(secret) * '*');
# show it
show_secret(None, None)

# tips array
tips = db_data[secret]

### MAIN ###

while(check_result()):
  # get first elem
  cur_tip = tips.pop(0)
  print(cur_tip)
  # and added to the end
  tips.append(cur_tip)
  # get sym from user
  answer = get_sym()
  # and check it
  print ( check_it(secret, answer) )



