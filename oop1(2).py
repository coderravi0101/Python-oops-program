# -*- coding: utf-8 -*-
"""oop1(2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WAGq_ZaiutgKvJzhZop8GKSGPyAMmGZc
"""



"""#Some magic  methods"""

class Temp:

  def __init__(self): # it is a constructor
    print('Hello word')

Ravi=Temp()   # obj=Temp()

#we create your own first data type which name is Fraction
class Fraction:
  # ab es class ke under hum variable dalenge accordingh to yourneed
 # parameterized costructor
  def __init__(self,x,y): # 1stmagic method
    self.num=x
    self.den=y

  def __str__(self):# 2nd magic method
   return '{}/{}'.format(self.num,self.den)

fr1=Fraction(3,7)
fr2=Fraction(2,11)

print(fr1)
print(fr2)