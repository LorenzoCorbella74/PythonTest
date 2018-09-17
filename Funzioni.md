## Funzioni
Le funzioni in Python sono oggetti che come in JS possono essere passate tra parti diverse di codice:

```Python
# define a basic function
def func1():
  print ("I am a function")

# function that takes arguments
def func2(arg1, arg2):
  print (arg1, " ", arg2)

# function that returns a value
def cube(x):
  return x*x*x

# function with default value for an argument
def power(num, x=1):
  result = 1;
  for i in range(x):
    result = result * num  
  return result

#function with variable number of arguments
def multi_add(*args): # * indica che passo un numero variabile di argomenti
  result = 0;
  for x in args:
    result = result + x
  return result

func1()
print (func1())
print (func1)   # la funzione non ritorna niente quindi è indicato " None "
func2(10,20)
print (func2(10,20))
print (cube(3))
print (power(2))
print (power(2,3))
print (power(x=3, num=2)) #  python considera i nomi degli argomenti che possono essere invertiti o scambiati, etc
print (multi_add(4,5,10,4)) 
```

[back](Note.md#indice)