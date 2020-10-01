import msvcrt

file = open("C:/Users/javie/Desktop/Programacion/Python/jumpyrinth/2c464e58-9121-11e9-aec5-34415dec71f2.txt", "r")

def move_down():
  file.seek(file.tell() + 1025)

stack = []
FLAG

######   MAIN PROGRAM   #######
file.seek(0)
c = file.read(1)
while c != '@':
  c = file.read(1)
  #print(c, end ="")
  if c == '$':
    move_down(1)
    #start path
  if c == '(':
    #pop from stack
    #prepend such char to FLAG string
    #read number on the right
    #jump to the left
  if c == ')':
    #pop from stack
    #prepend such char to FLAG string
    #read number on the left
    #jump to the right
  if c == '-':
    #remove first char from FLAG
    #jump above by the number specified below
  if c == '+':
    #remove first char from FLAG
    #read number above
    #jump below
  if c == '%':
    #Reverse FLAG
    #Go down 1 position
  if c == '[':
    #Read char to the right
    #Push it into STACK
    #jump again to right [cx  ends in x
  if c == ']':
    #Read character to the left
    #push it into STACk
    #jump to the left again
  if c == '*':
    
  if c == '.':

  if c == '<':

  if c == '>':
  
  if c == '^':
  if c == 'v':
      
