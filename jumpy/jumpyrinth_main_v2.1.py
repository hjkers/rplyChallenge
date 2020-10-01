#A new version.
#Now, STACK and FLACK are both lists. FLAG will be later converted into string.

"""
v2.2
jump_below(n) implemented

read_above() implemented
read_below() implemented
"""

STACK = []
FLAG  = []

file = open("2c464e58-9121-11e9-aec5-34415dec71f2.txt", "r")

#This function has been tested and works.
def read_right():
  n = ""
  c = file.read(1)
  while c <= '9' and c >= '0':
    n += c
    c = file.read(1)
  m = int(n)
  return m

#I think it works?...
def read_left():
  file.seek(file.tell() - 1)
  n = ""
  c = file.read(1)
  while c >= '0' and c <= '9':
    n += c
    if file.tell() >= 2:
      file.seek(file.tell() - 2)
      c = file.read(1)
    else:
      break
  return int(n)

def jump_above(n):
  if (file.tell() - n*1026) >= 0:
    file.seek(file.tell() - n*1026)
  else:
    print("Jump could not be done!")

#I think this... works? wtf?
def jump_below(n):
  file.seek(file.tell() + n*1026)

def read_above():
  n = ""
  jump_above(1)
  c = file.read(1)
  file.seek(file.tell()-1)
  while c >= '0' and c <= '9':
    n += c
    if file.tell() > 1025:
      jump_above(1)
      c = file.read(1)
      file.seek(file.tell()-1)
    else:
      break
  if n == "":
    return -1
  else:
    return int(n)

def read_below():
  n = ""
  jump_below(1)
  c = file.read(1)
  file.seek(file.tell()-1)
  while c >= '0' and c <= '9':
    n += c
    jump_below(1)
    c = file.read(1)
    file.sek(file.tell()-1)
  return int(n)

begin = 0
banderica = ""

def retry(begin, STACK):
  #### MOVE TO $ SYMBOL ####
  symbol = ' '
  print("By which symbol $ start?: ")
  count = 0
  while count < begin:
    symbol = file.read(1)
    if symbol == '$':
      count += 1
  file.seek(file.tell()-1) #Restore position after reading last $

  #### MAIN LOOP ####
  c = 'a'
  while c != '@':
    c = file.read(1)
    file.seek(file.tell() - 1)
    if c == '#':
      print("Nothing is done")
    if c == '(':
      FLAG = STACK.pop() + FLAG
      pos = file.tell()
      n = read_right()
      file.seek(pos - n)
    if c == ')':
      FLAG.append(STACK.pop())
      pos = file.tell()
      n = read_left()
      file.seek(pos + n)
    if c == '-':
      del FLAG[0]
      pos = file.tell()
      n = read_below()
      file.seek(pos)
      jump_above(n)
    if c == '+':
      FLAG.pop()
      pos = file.tell()
      n = read_above()
      file.seek(pos)
      jump_below(n)
    if c == '%':
      FLAG = FLAG[::-1]
      jump_below(1)
    if c == '[':
      file.seek(file.tell()+1)
      STACK += file.read(1)
    if c == ']':
      file.seek(file.tell()-1)
      STACK.append(file.read(1))
      file.seek(file.tell()-2)
    if c == '*':
      jump_above(1)
      char = file.read(1)
      file.seek(file.tell() - 1)
      STACK.append(char)
      jump_above(1)
    if c == '.':
      jump_below(1)
      char = file.read(1)
      file.seek(file.tell()-1)
      STACK.append(char)
      jump_below(1)
    if c == '<':
      pos = file.tell()
      n = read_right()
      file.seek(pos - n)
    if c == '>':
      pos = file.tell()
      n = read_left()
      file.seek(pos + n)
    if c == '^':
      pos = file.tell()
      n = read_below()
      file.seek(pos)
      jump_above(n)
    if c == 'v':
      pos = file.tell()
      n = read_above()
      file.seek(pos)
      jump_below(n)
    if c == '@':
      #CHECK FLAG
      for elem in FLAG:
        banderica += elem
      #End of the path
      break
  if banderica == "":
    begin += 1 #retry path by the next $
    file.seek(0)
    retry(begin, STACK)


retry(begin, STACK)
print("LA BANDERITA FINAL WEY: ", banderica)
file.close()
