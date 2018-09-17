## Moduli
I moduli, (conosciuti come librerie in altri linguaggi), sono dei file usati per raggruppare costanti, funzioni e classi, che ci consentono di suddividere e organizzare meglio i nostri progetti. Python include già una lista estensiva di moduli standard (standard library), ma è anche possibile scaricarne o definirne di nuovi.

```Python
# GLOBALE
>>> import math  # importiamo il modulo math della libreria standard
>>> math  # l'import crea una nuova variabile che si riferisce al module
>>> help(math)  #  help() permette di vedere la documentazione del modulo

# SINGOLA FUNZ
>>> from math import pi, sqrt  # importa solo i nomi pi e sqrt dal modulo math
>>> pi  # è ora possibile accedere a pi senza usare math.pi -> 3.141592653589793
>>> sqrt  # è ora possibile accedere a sqrt senza usare math.sqrt

# ALIAS
>>> import math as matematica  # importa il modulo math chiamandolo matematica
>>> matematica.pi  # possiamo accedere agli oggetti di math facendo matematica.nome -> 3.141592653589793

>>> from math import sqrt as radice_quadrata  # importa sqrt chiamandolo radice_quadrata
>>> radice_quadrata  # radice_quadrata si riferisce lo stesso a sqrt

# TUTTO
>>> from math import *  # importa tutti i nomi definiti nel modulo math
>>> pi  # possiamo ora accedere direttamente a tutti i nomi di math -> 3.141592653589793
```

[back](Note.md#indice)