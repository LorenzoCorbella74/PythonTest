import tobeimported

globalona = "funziona!"

def main():
    print("Test: "+globalona)
    #nome = input('Inserisci il tuo nome: ')
    #print(nome)

# si mette tutto dentro un dictionary
class Accumulator:
    # inizializza la classe
    def __init__(self):
        self.total = 0

    def add(self, x):
        self.total += x

class Store:
    # funzione speciale che inizializza la classe
    def __init__(self):
        self.store = {}

    def set(self, key,value):
        self.store[key] = value

    def get(self,key):
        return self.store[key]

# una funzione innestata ha accesso allo scope della funzione che lo contiene
# e questo non è nè lo scope locale nè quello globale
def calc(x):
    # Variables defined inside a function or class, are not global. 
    # Only the function or class can see the variable:
    a = 1
    def twice():
        return x * 2 + a

    return twice() + 5

def calc2(x):
    z = 10
    def twice():
        # Se la variabile interna si chiama come quella nello scope esterno 
        # er prevenire il problema UnboundLocalError: local variable 'z' referenced before assignment
        # si specifica che non è una variabile locale (ma nenanche una globale) con la keywor "nonlocal": 
        # è stato aggiunto da Python 3 
        # SOurce: https://www.ynonperek.com/2017/09/11/python-variable-scope-implicit-global-and-nonlocal/
        nonlocal z
        z *= 20

    twice()
    twice()
    twice()
    return z + 10


if __name__=="__main__": # indica che è la partenza di tutto!
    main()
    a = Accumulator()
    a.add(1)
    a.add(2)
    a.add(4)
    print(a.total)  # This works. Prints 7
    print(calc(10)) # Prints 26
    print(calc2(10))
    # print(globals()) # prints global namespace
    # print(locals()) # prints local namespace
    s = Store()
    s.set('nome','Lorenzo')
    print(s.get('nome'))
    tobeimported.print_func("Chiara")    # esempio di funzione importata da un altro file


