#!/usr/bin/env python3

class MyString:
  def __init__(self, value =""):
    if type(value) == str:
      self.value = value
      print(value)
    else:
      print("The value must be a string.")
  

myword = MyString(True)

