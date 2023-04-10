# -*- coding: utf-8 -*-
"""Gabarito - Listas 09.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HCMtMJHvIY3eOhIcvtK4j5U1-3pkG9Kw

# Copiar e "Igualdade" de Listas

### Estrutura:

- Quando fazemos:<br>
lista2 = lista1<br>
não estamos criando uma lista nova, mas estamos atribuindo outra variável à mesma lista.

- Se quisermos copiar lista devemos fazer<br>
lista2 = lista1.copy()<br>
ou entao<br>
lista2 = lista1[:]

Para entender bem isso, vamos ver na prática:
"""

lista = ['ipad', 'iphone x', 'apple tv']
lista2 = lista

lista[1] = 'iphone 11'

print(lista)
print(lista2)

"""### Agora copiando:"""

lista = ['ipad', 'iphone x', 'apple tv']
lista2 = lista[:]

lista[1] = 'iphone 11'
print(lista)
print(lista2)