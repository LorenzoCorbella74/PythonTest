
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

  [back](Note.md#indice)