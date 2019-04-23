import stack as stack
from decimal import Decimal

def isOp(string):
  return string == "+" or string == "-" or string == "*" or string == "/"

print("Enter equation in Polish Notation seperated by spaces")
print("(Enter \"exit\" to exit)")

while True:
  valid = True
  equation = input()
  if equation == "exit":
    break
  equation = equation.split()
  for e in equation :
    if e == " ":
      continue
    if isOp(e):
      t1 = Decimal(stack.pop())
      t2 = Decimal(stack.pop())
      total = t2 + t1 if e == "+" else t2 - t1 if e=="-" else t2 * t1 if e=="*" else t2 / t1 if e=="/" else 0
      stack.push(total)
    elif not e.replace('.','',1).isdigit():
      valid = False
      break
    else:
      stack.push(e)
  if valid:
    valid = False if stack.stackSize() != 1 else True
  if valid:
    print(stack.pop())
  else:
    print("Invalid Input")
    stack.empty()
