"""
Argumenty kluczowe i pozycyjne
kluczowy w postaci: klucz - wartość (domyślny)
Pozycyjne - takich, których liczy się kolejność przy wywołaniu
"""

def greet(name, message='Hello', separator=' '):
    print(message, name, sep=separator,end='\n')


greet("Arek", 'Witojcie')
greet("Arek", 'Witojcie', '_')
greet("Justyna", separator='.')
greet("Justyna", separator='\n')

greet(message='Witojcie', name='Arek')