class MyString():
  def __init__(self,strng=""):
    self.strng = str(strng)
    self._data_len = len(strng)
    
  def __str__(self):
    return self.strng
    
  def __repr__(self):
    return self.strng
    
  def __len__(self):
    return self._data_len
  
  def __gt__(self,other):
    if len(self) > len(other):
      return True
    else:
      return False
      
  def __sub__(self,other):
    if len(self) > len(other):
      return len(self) - len(other)
    else:
      return len(other) - len(self) 