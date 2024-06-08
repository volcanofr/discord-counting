from utils.isType import isNumber, isInteger

import base64

def toNumber(number):
  try:
    value = isNumber(str(number))
    if type(value) == float:
      return str(value)
    else:
      return False
  except:
    return False
  
def toInteger(number):
  try:
    value = isInteger(str(number))
    if type(value) == int:
      return str(value)
    else:
      return False
  except:
    return False
  
def toBase64(number):
  try:
    if type(number) != int:
      return False
    else:
      value = base64.b64encode(str(number).encode("utf-8")).decode("utf-8")
      return value
  except:
    return False
  
def toHex(number):
  try:
    if type(number) != int:
      return False
    else:
      value = hex(number)[2:]
      return value
  except:
    return False

def toLetter(number):
  try:
    if type(number) != int:
      return False
    else:
      result = ''
      num = number
      while num > 0:
        num -= 1
        result = chr(num % 26 + 65) + result
        num //= 26
      return result
  except:
    return False