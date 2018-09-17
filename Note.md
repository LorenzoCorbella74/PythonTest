# Appunti di Python

## Indice
 - [Intro](#intro)
 - [Variabili](#variabili)
 - [Scope di variabili](#scope-di-variabili)
 - [Tipi](Tipi.md)
    - [Tuple](Tipi.md#tuple)  
    - [Liste](Tipi.md#liste)  
    - [Dizionari](Tipi.md#dizionari)  
    - [Conversioni](Tipi.md#conversioni)  
 - [Funzioni](Funzioni.md)
 - [Espressioni](Espressioni.md)
 - [Condizioni](Condizioni.md)
 - [Loops](Loops.md#loops)
 - [Recuperare dati dal WWW](request.md)
 - [OOP e classi](Classi.md)


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

[back](Note.md#indice)

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

""" A differenza di JS variabili di differenti tipi non possono essere combinati: 
# print ("string type " + 123) -> dà errore
# print ("string type " + str(123))   # corretta """

A differenza di JavaScript, Python non ha il concetto di 'undefined'. Invece, ciò che normalmente farebbe ritornare un undefined in Javascript semplicemente genera in Python una eccezione. Inoltre l'analogo di 'null' in JS è 'None'.
```Python
>>> "a string".foo    # AttributeError: 'str' object has no attribute 'foo'

```

[back](Note.md#indice)

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
[back](Note.md#indice)