## Tipi di dati
I tipi di dato possono essere immutabili o mutabili. I numeri (int, float, complex, bool), le stringhe (str), i bytes, e i frozenset sono immutabili; le liste (list), gli insiemi (set), e i dizionari (dict) sono invece mutabili.

    - Intero	    int	    Intero di dimensione arbitraria	-42, 0, 1200, 999999999999999999
    - Reale	        float	Numero a virgola mobile	3.14, 1.23e-10, 4.0E210
    - Booleano	    bool	Per valori veri o falsi	True, False
    - Complesso	    complex	Numeri complessi con parte reale e immaginaria	3+4j, 5.0+4.1j, 3j
    - Stringhe	    str	    Usata per rappresentare testo	'', 'stefano', "l'acqua"
    - Bytes	        bytes	Usata per rappresentare bytes	b'', b'\x00\x01\x02', b'Python'
    - Liste	        list	Una sequenza mutabile di oggetti	[], [1, 2, 3], ['Hello', 'World']
    - Tuple	        tuple	Una sequenza immutabile di oggetti	(), (1, 2, 3), ('Python', 3)
    - Insiemi	    set/frozenset	Un’insieme di oggetti unici	{1, 2, 3}, {'World', 'Hello'}
    - Dizionari	    dict	Una struttura che associa chiavi a valori	{}, {'nome': 'Ezio', 'cognome': 'Melotti'}

[back](Note.md#indice)

### Tuple
E' una sequenza immutabile di oggetti eterogenei, quindi una volta create non è possibile aggiungere, rimuovere, o modificare gli elementi. E' racchiusa tra '()'.

```Python
>>> t = ('abc', 123, 45.67)
>>> t[0]  # le tuple supportano indexing -> 'abc'
>>> t[:2]  # slicing    -> ('abc', 123)
>>> 123 in t  # gli operatori di contenimento "in" e "not in"   -> True
>>> t + ('xyz', 890)  # concatenazione (ritorna una nuova tupla) -> ('abc', 123, 45.67, 'xyz', 890)
>>> t * 2  # ripetizione (ritorna una nuova tupla) -> ('abc', 123, 45.67, 'abc', 123, 45.67)
>>> len(('abc', 123, 45.67, 'xyz', 890))  # numero di elementi  -> 5
>>> min((4, 1, 7, 5))  # elemento più piccolo -> 1
>>> max((4, 1, 7, 5))  # elemento più grande -> 7
>>> t = ('a', 'b', 'c', 'b', 'a')
>>> t.index('c')  # indice dell'elemento 'c'    -> 2
>>> t.count('c')  # numero di occorrenze di 'c' -> 1
>>> t.count('b')  # numero di occorrenze di 'b' -> 2
```
[back](Note.md#indice)

### Liste
Le liste sono "mutabili" a lunghezza variabile vengono definite elencando tra parentesi quadre ([]) una serie di oggetti separati da virgole ','. È possibile creare una lista vuota usando le parentesi quadre senza nessun elemento all’interno.
```Python
>>> letters = ['a', 'b', 'c', 'd', 'e']
>>> letters[0]  # le liste supportano indexing ->'a'
>>> letters[-1] # -> 'e'
>>> letters[1:4]  # slicing -> ['b', 'c', 'd']
>>> 'a' in letters  # gli operatori di contenimento "in" e "not in" -> True
>>> letters + ['f', 'g', 'h']  # concatenazione (ritorna una nuova lista) -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
>>> [1, 2, 3] * 3  # ripetizione (ritorna una nuova lista) -> [1, 2, 3, 1, 2, 3, 1, 2, 3]


""" METODI
lista.append(elem):   aggiunge elem alla fine della lista;
lista.extend(seq):    estende la lista aggiungendo alla fine gli elementi di seq;
lista.insert(indice, elem): aggiunge elem alla lista in posizione indice;
lista.pop(): rimuove e restituisce l’ultimo elemento della lista;
lista.remove(elem): trova e rimuove elem dalla lista;
lista.sort(): ordina gli elementi della lista dal più piccolo al più grande;
lista.reverse(): inverte l’ordine degli elementi della lista;
lista.copy(): crea e restituisce una copia della lista; """
```
[back](Note.md#indice)

### Dizionari
E' l'analogo dell'oggetto in JS, ossia un insieme non ordinato di item chiave (univoca, stringhe, interi, tuple) valore
```Python
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> d['a']  # ritorna il valore associato alla chiave 'a' -> 1
>>> d['c']  # ritorna il valore associato alla chiave 'c' -> 3
>>> d['x']  # se la chiave non esiste restituisce un KeyError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'x'
>>> 'x' in d  # la chiave 'x' non è presente in d -> False
>>> 'x' not in d  # la chiave 'x' non è presente in d ->True
>>> 'b' in d  # la chiave 'b' è presente -> True
"""
METODI
d.items()	Restituisce gli elementi di d come un insieme di tuple
d.keys()	Restituisce le chiavi di d
d.values()	Restituisce i valori di d
d.get(chiave, default)	Restituisce il valore corrispondente a chiave se presente, altrimenti il valore di default (None se non specificato)
d.pop(chiave, default)	Rimuove e restituisce il valore corrispondente a chiave se presente, altrimenti il valore di default (dà KeyError se non specificato)
d.popitem()	Rimuove e restituisce un elemento arbitrario da d
d.update(d2)	Aggiunge gli elementi del dizionario d2 a quelli di d --> MERGE!!
d.copy()	Crea e restituisce una copia di d
d.clear()	Rimuove tutti gli elementi di d
"""

>>> d = {'a': 1, 'b': 2, 'c': 3}  # nuovo dict di 3 elementi
>>> len(d)  # verifica che siano 3

>>> d.items()  # restituisce gli elementi
dict_items([('c', 3), ('a', 1), ('b', 2)])

>>> d.keys()  # restituisce le chiavi
dict_keys(['c', 'a', 'b'])

>>> d.values()  # restituisce i valori
dict_values([3, 1, 2])

>>> d.get('c', 0)  # restituisce il valore corrispondente a 'c' -> 3
>>> d.get('x', 0)  # restituisce il default 0 perché 'x' non è presente -> 0
>>> d  # il dizionario contiene ancora tutti gli elementi

{'c': 3, 'a': 1, 'b': 2}
>>> d.pop('a', 0)  # restituisce e rimuove il valore corrispondente ad 'a' -> 1
>>> d.pop('x', 0)  # restituisce il default 0 perché 'x' non è presente -> 0
>>> d  # l'elemento con chiave 'a' è stato rimosso
{'c': 3, 'b': 2}

>>> d.pop('x')  # senza default e con chiave inesistente dà errore
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'x'

>>> d.popitem()  # restituisce e rimuove un elemento arbitrario
('c', 3)

>>> d  # l'elemento con chiave 'c' è stato rimosso -> {'b': 2}

>>> d.update({'a': 1, 'c': 3})  # aggiunge di nuovo gli elementi 'a' e 'c'
>>> d # {'c': 3, 'a': 1, 'b': 2}
>>> d.clear()  # rimuove tutti gli elementi
>>> d  # lasciando un dizionario vuoto -> {}
```

[back](Note.md#indice)

### __dict__
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

[back](Note.md#indice)

### Conversioni
 In Python il tipo è legato all’oggetto stesso e non può essere cambiato. Questo vuol dire che non è possibile convertire (cast) una variabile o un oggetto da un tipo ad un altro. Dato che il tipo di un oggetto non può essere cambiato, in Python la conversione non modifica l’oggetto originale, ma ne crea di nuovi a partire da oggetti già esistenti. Questa operazione può essere effettuata passando l’oggetto che vogliamo convertire al tipo in cui lo vogliamo convertire. Ad esempio, se vogliamo convertire una lista in un insieme possiamo usare set(lista):

```Python
>>> mylist = [1, 2, 3, 2, 1]  # definisco una lista
>>> myset = set(mylist)       # creo un nuovo insieme a partire dalla lista
>>> myset                     # l'insieme contiene gli stessi elementi (senza duplicati)
{1, 2, 3}
>>> mylist                    # la lista originale esiste ancora
[1, 2, 3, 2, 1]

# Se vogliamo, invece, convertire una stringa in numero, possiamo procedere come segue:
>>> mystr = '3.14'            # definisco una stringa
>>> myfloat = float(mystr)    # creo un nuovo float a partire dalla stringa
>>> myfloat                   # il float corrisponde al numero della stringa    -> 3.14
>>> mystr                     # la stringa originale esiste ancora              -> '3.14'
```
È anche possibile convertire una lista di tuple in un dizionario:
```Python
>>> mylist = [('a', 1), ('b', 2), ('c', 3)]
>>> mydict = dict(mylist)
>>> mydict
{'c': 3, 'a': 1, 'b': 2}
```

Ogni tipo accetta diversi input, ma non tutte le conversioni sono possibili. Ad esempio, non è possibile convertire una lista in intero, o un intero in lista. Se passiamo un oggetto che non può essere convertito, Python restituirà un TypeError o un ValueError:

```Python
>>> int('un milione')  # str è un tipo valido, ma il valore non può essere convertito
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'un milione'
>>> int([1, 2, 3])     # list non è un tipo valido, quindi un TypeError viene restituito
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
</module></stdin></module></stdin>
```

È anche possibile creare copie di un oggetto senza cambiarne il tipo. Ad esempio:

```Python
>>> mylist1 = [1, 2, 3]      # creo una lista
>>> mylist2 = list(mylist1)  # creo una nuova lista (una copia) partendo da mylist1
>>> mylist2                  # la copia contiene gli stessi elementi dell'originale
[1, 2, 3]
>>> mylist1.append(4)        # posso modificare l'originale aggiungendo un elemento
>>> mylist1                  # l'elemento viene aggiunto alla lista originale
[1, 2, 3, 4]
>>> mylist2                  # ma non alla copia
[1, 2, 3]
```

[back](Note.md#indice)