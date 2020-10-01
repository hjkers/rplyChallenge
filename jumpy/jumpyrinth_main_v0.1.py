import msvcrt

file = open("C:/Users/javie/Desktop/Programacion/Python/jumpyrinth/2c464e58-9121-11e9-aec5-34415dec71f2.txt", "r")

STACK = []
FLAG = ""

### INTERFACE ###
"""
move_down(int m)
move_up(int m)
move_left(int m)
move_right(int m)

read_down() : int
read_up()   : int
read_left()

read_right(): int
"""
#### FUNCTIONS ####
def read_left():
  pos = file.tell()
  file.seek(file.tell() - 2)
  c = file.read(1)
  n = ""
  while (c <= '9' and c >= '0'):
    file.seek(file.tell() - 2)
    n += c
    file.seek(file.tell() - 2)
    c = file.read(1)
  m = int(n[::-1])
  file.seek(pos)
  return m

def read_right():
  pos = file.tell()
  file.seek(pos)
def read_down():
  pos = file.tell()
  file.seek(pos)
  return n

def read_up():
  pos = file.tell()
  file.seek(pos)
  return n

def move_down(m):
  file.seek(file.tell() + m*1025)
  
def move_up(m):
  file.seek(file.tell() - m*1025)
def move_right(m):
  file.seek(file.tell() + m)
def move_left(m):
  file.seek(file.tell() - m)

######   MAIN PROGRAM   #######
file.seek(0)
c = ' '
start = False
while not start:
  c = file.read(1)
  print(c, end ="")
  if c == '$':
    file.seek(file.tell()-1)
    move_down(1)
    start = True


while c != '@':
  if c == '(':
    FLAG = chr(STACK.pop()) + FLAG
    m = read_right()#read number on the right
    move_left(m)
  if c == ')':
    FLAG += chr(STACK.pop())
    m = read_left()#read number on the left
    move_right(m)
  if c == '-':
    FLAG = FLAG[1:len(FLAG)]
    move_up(read_down())
  if c == '+':
    FLAG = FLAG[0:len(FLAG)-1]
    move_down(read_up())
  if c == '%':
    FLAG = FLAG[::-1]
    move_down(1)
  if c == '[':
    char = file.read(1)
    STACK.append(char)
    file.read(1)
  if c == ']':
    char = file.seek(file.tell() - 1)
    STACK.append(char)
    file.seek(file.tell() - 1)
  if c == '*':
    char = file.seek(file.tell() - 1026)
    STACK.append(char)
    file.seek(file.tell() - 1026)
  if c == '.':
    char = file.seek(file.tell() + 1024)
    STACK.append(char)
    file.seek(file.tell() + 1024)
  if c == '<':
    move_left(file.read(2))
  if c == '>':
    move_right(read_left())
  if c == '^':
    move_up(read_down())
  if c == 'v':
    move_down(read_up())


print("The FLAG is: ", FLAG)
