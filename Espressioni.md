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

[back](Note.md#indice)