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

[back](Note.md#indice)