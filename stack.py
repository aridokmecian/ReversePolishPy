stack = []
size = 0

def push(element) :
  global size
  if 1000 > size:
    size = size + 1
    stack.append(element)
  else:
    print("Too Many elements in stack")
  
def pop():
  global size
  if size > 0 :
    size = size - 1
    return stack.pop()
  else:
    print("Empty Stack")
  
def peek():
  return stack[size - 1]

def stackSize() :
  return size

def empty():
  for x in range(0, size):
    pop()