## Classi
L'argomento "self" è tipo il "this" di JS e si riferisce alla specifica istanza della classe.  

```Python
class myClass:

  def method1(self):
    print ("myClass method1")
    
  def method2(self, someString):
    print ("myClass method2: " + someString)
    
class anotherClass(myClass):    #eredita dalla 1° classe
  def method2(self):            # override del metodo della classe ereditata
    print ("anotherClass method2") 
    
  def method1(self):
    myClass.method1(self);  # si chiama il metodo della classe ereditata
    print ("anotherClass method1")
      
def main():
  c = myClass()             # qua si crea (senza il new...)
  c.method1()               # si chiama i metodi della classe senza dover fornire il self che è dato automaticamente dal python runtime
  c.method2("This is a string")
  c2 = anotherClass()   
  c2.method1()

# Python class with dict-like get/set item
# SOURCE: https://gist.github.com/turicas/1510860

```