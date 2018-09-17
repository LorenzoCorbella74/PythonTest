# Appunti di Python

## Indice
 - [Intro](#intro)
 - [Variabili](#variabili)
 - [Scope di variabili](#scope-di-variabili)
 - [Funzioni](#funzioni)
 - [Espressioni](#espressioni)
 - [Condizioni](#condizioni)
 - [Loops](#loops)
 - [Classi](#classi)
 - [Recuperare dati dal WWW](request.md)
 - [OOP e classi](classi.md)


## INTRO

Python è un linguaggio interpretato come Js, cioè non deve essere compilato come java e buildato in un eseguibile ma è interpretato ed eseguito direttamente. Ogni volta che viene invocato il comando python, il codice scritto viene scansionato per token, ognuno dei quali viene analizzato dentro una struttura logica ad albero che rappresenta il programma. Tale struttura viene, infine, trasformata in bytecode (file con estensione .pyc o .pyo). Per potere eseguire questi bytecode, si utilizza un apposito interprete noto come macchina virtuale Python (PVM).
E' possibile far girare l'interpreter Python in CLI (interpreted mode) tramite il comando `> python` (`exit()` per uscire) o eseguire del codice tramite `> python nomefile.py`. Python a differenza di JS identifica i blocchi in base all'indentazione del codice: nelle funzioni e nelle condizioni ':' identifica l'inizio dello scope block.

```Python
def main():
    print("Hello world")
    input('Inserisci il tuo nome: ')

if __name__=="__main__": # indica che è la partenza di tutto!
    main()
```

## Variabili
Ogni nome di variabile deve iniziare con una lettera o con il carattere underscore (_), e può essere seguita da lettere, numeri, o underscore; esistono delle parole riservate (keyword) che non possono essere utilizzate come nomi di variabili: False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield; Python è un linguaggio case-sensitive, che distingue tra nomi di variabili composti da caratteri minuscoli e maiuscoli;
In Python 3 è possibile (ma generamente sconsigliato) usare caratteri accentati o in altri alfabeti nei nomi delle variabili

```Python
myint = 7           # intero

myfloat = 7.0
myfloat = float(7)  # float

mystring = 'hello'  # stringhe
mystring = "hello"
mystring = "Non preoccuparti dell'apostrofo"

myboolean = True    # sono maiuscoli !!!
myboolean = False   # sono maiuscoli !!!

one = 1
two = 2
three = one + two  # somma

hello = "hello"
world = "world"
helloworld = hello + " " + world # concatenazione stringhe

f,e,d = 0,1,2 # assegnazione multipla

# si modificano le variabilisemplicemente riassegnandole
f = "abc"

# A differenza di JS variabili di differenti tipi non possono essere combinati: 
# print ("string type " + 123) -> dà errore
# print ("string type " + str(123))   # corretta
```

A differenza di JavaScript, Python non ha il concetto di 'undefined'. Invece, ciò che normalmente farebbe ritornare un undefined in Javascript semplicemente genera in Python una eccezione. Inoltre l'analogo di 'null' in JS è 'None'.
```Python
>>> "a string".foo    # AttributeError: 'str' object has no attribute 'foo'

```

### Scope di variabili
Relativamente a variabili locali o globali se dichiaro una variabile dentro una funzione con lo stesso nome di una variabile esterna alla funziona l'interpreter le considera variabili diverse. Se invece voglio che quella interna si riferisca a quella esterna si deve specificare:
```Python

# SOURCE: https://www.ynonperek.com/2017/09/11/python-variable-scope-implicit-global-and-nonlocal/
_total = 0

def add(x):
    _total += x
      # Error: UnboundLocalError: local variable '_total' referenced before assignment
add(1)
add(2)
add(4)

# Mentre se ci si referenzia alla variabile "globale" fuori dalla funzione
_total = 0

def add(x):
    global _total
    _total += x

add(1)
add(2)
add(4)

# OK - prints 7
print(_total)

# Nel caso in cui si abbiano funzioni innestate


del f   # cancella la definizione di una variabile precedentemente dichiarata
print(f)
```

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
# Espressioni
```Python
>>> 9 & 1              # Bitwise operations
>>> 2 << 2             # Shifting
>>> 5 >= 3             # Comparisons
>>> 8 + 2 * (3 + 5)    # Arithmetic
>>> 1 == 1             # Equivalence

# Some C-like expression constructs have been substituted for more readable alternatives:

>>> not True           # 'not' instead of '!'
>>> True and True      # 'and' instead of '&&'
>>> True or False      # 'or' instead of '||'

# But there's some elements of C-like expressions that aren't supported, because they tend to be more trouble than they're  worth. For instance, some constructs that can be used in expressions in C-like languages can only be used in statements in Python:

>>> a = 5              # Assignment works in statements.
>>> a += 1             # Add-assignment does too.
>>> if a = 1:          # But you can't assign in an expression. ->SyntaxError: invalid syntax
# The ++ and -- unary assignment operators aren't part of the Python language.
```

## __dict__
L'attributo contiene tutti gli attributi che descrivono l'oggetto in questione. Può essere usato per alterare o leggere gli attributi. In Python tutto è un oggetto, functions, classes, objects etc:

```Python
def func():
    pass  #equivale ad un operazione nulla

func.temp = 1

print func.__dict__

class TempClass(object):
    a = 1
    def tempFunction(self):
        pass

print TempClass.__dict__
# Output

 {'temp': 1}

 {'a': 1, '__module__': '__main__', 'tempFunction': <function tempFunction at 0x7f77951a95f0>, '__dict__': <attribute '__dict__' of 'TempClass' objects>, 
'__weakref__': <attribute '__weakref__' of 'TempClass' objects>, '__doc__': None}

```

## Condizioni
Python non ha nè "switch-case" nè "do...while" loop e al posto dell'operatore ternario ha il così detto "conditional statement" per avere tutto su ura sola riga di codice:

```Python
# conditional flow uses if, elif, else  
  if(x < y):
    st= "x is less than y"
  elif (x == y):    # uguaglianza!
    st= "x is same as y"
  else:
    st= "x is greater than y"
  print (st)

  # conditional statements let you use "a if C else b"
  st = "x is less than y" if (x < y) else "x is greater than or equal to y"
  print (st)
  ```

## Loops
Ha solo due possibilità di fare loop, while e for loop. Questi ultimi sono degli iteratori.

```Python
   x = 0
  
  # define a while loop
  while (x < 5): # condizione
     print (x)
     x = x + 1  # condizione

  # define a for loop
  for x in range(5,10): # si va da 5 a 9, il 10 NON è CONSIDERATO!
    print (x)
    
  # use a for loop over a collection
  days = ["Mon","Tue","Wed","Thu","Fri"]
  for d in days:
    print (d)
  
  # use the break and continue statements
  for x in range(5,10):
    #if (x == 7): break
    #if (x % 2 == 0): continue
    print (x)
  
  #using the enumerate() function to get index 
  days = ["Mon","Tue","Wed","Thu","Fri"]
  for i, d in enumerate(days):
    print (i, d) # i è l'indice e d è il value

```


