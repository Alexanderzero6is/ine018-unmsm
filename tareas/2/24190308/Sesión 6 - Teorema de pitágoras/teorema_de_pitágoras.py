# -*- coding: utf-8 -*-
"""Teorema de Pitágoras

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PS8reZ4ht2ygp1sye8j5kYlWa7cDN0cH
"""

from math import sqrt

a = float(input("Ingresa el primer cateto: "))
b = float(input("Ingresa el segundo cateto: "))

h = sqrt(a * a + b * b)

print("La hipotenusa es: ", h)