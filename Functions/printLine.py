# def printLine(text):
#   print(text, 'is awesome.')
#
# printLine('Python')
#
# def greetPerson(*name):
#   print('Hello', name)
#
# greetPerson('Frodo', 'Sauron')

# result = lambda x: x * x
# print(result(5))

def Foo(x):
  if (x==1):
    return 1
  else:
    return x+Foo(x-1)

print(Foo(4))