# -*- coding: utf-8 -*-
"""triangle

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vg2l-XKYGr7-WFzJXnHAfAf7GkcXTQm0
"""

# triangle.py

n = int(input("Please input line number:"))
for i in range(n):
  line = " " * (n - 1 - i) + "@" * (2 * i + 1)
  print(line)
