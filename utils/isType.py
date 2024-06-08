import math
import base64

def isNumber(string):
  try:
    value = float(string)
    if math.isnan(value) or math.isinf(value):
      return False
    else:
      return value
  except:
    return False

def isInteger(string):
  try:
    value = int(string)
    if math.isnan(value) or math.isinf(value):
      return False
    else:
      return value
  except:
    return False
  
def isBase64(string):
  try:
    decoded = base64.b64decode(string, validate=True)
    try:
      value = decoded.decode("utf-8")
      return isInteger(value)
    except:
      return False
  except:
    return False
  
def isHex(string):
  try:
    value = int(string, 16)
    return isInteger(value)
  except:
    return False

def isLetter(string):
  try:
    value = sum((ord(char.lower()) - 96) for char in string)
    return isInteger(value)
  except:
    return False