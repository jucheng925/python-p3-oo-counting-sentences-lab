#!/usr/bin/env python3
import re

class MyString:
  def __init__(self, value =""):
    self.value = value
  
  def get_value(self):
    return self._value
  def set_value(self, value=""):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")
  value = property(get_value, set_value)

  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    end_list = re.findall(r'\b[.?!]*', self.value)
    end_list = ' '.join(end_list).split()
    return len(end_list)



