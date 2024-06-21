pasteNext = True

from utils.colors import COLORS
from utils.isType import isNumber, isInteger, isBase64, isHex, isLetter
from utils.toType import toNumber, toInteger, toBase64, toHex, toLetter

import pyperclip
import pynput.keyboard as Keyboard

print(COLORS["Reset"] + "\n" + COLORS["Cyan"] + "Starting volcanofr's automatic counting copy." + COLORS["Reset"] + "\n")

counted = 0
removed = 0
next = False

# Types: Base64, Hexadecimal, letter, number
countType = input(COLORS["Reset"] + COLORS["Blue"] + "Which channel type are you counting on? (Base64, Hexadecimal, letter, number, integer) " +
                  COLORS["Underline"] + COLORS["Bold"] + COLORS["BlueBright"])
if countType not in ("Hexadecimal", "Base64", "letter", "number", "integer"):
  print(COLORS["Reset"] + COLORS["Red"] + "Wrong channel type! Please use one of these: Base64, Hexadecimal, letter, number, integer" + COLORS["Reset"] + "\n")
  exit()
# print(COLORS["Reset"] + COLORS["BlueBright"] + "'{0}' has been selected as channel type.".format(countType) + COLORS["Reset"])

# Increment: any number
countIncrement_ = input(COLORS["Reset"] + COLORS["Blue"] + "What is your personnal increment for counting? (any number, ex: -0.01) " +
                        COLORS["Underline"] + COLORS["Bold"] + COLORS["BlueBright"])
if countType == "number":
  countIncrement = isNumber(countIncrement_)
  if countIncrement == False:
    print(COLORS["Reset"] + COLORS["Red"] + "Wrong increment! Please use any number for {0} channel".format(countType) + COLORS["Reset"] + "\n")
    exit()
else:
  countIncrement = isInteger(countIncrement_)
  if countIncrement == False:
    print(COLORS["Reset"] + COLORS["Red"] + "Wrong increment! Please use any integer for {0} channel".format(countType) + COLORS["Reset"] + "\n")
    exit()
# print(COLORS["Reset"] + COLORS["BlueBright"] + "'{0}' has been selected as increment.".format(countIncrement) + COLORS["Reset"])

# Last: (channel type) number
countLast_ = input(COLORS["Reset"] + COLORS["Blue"] + "What is the last counted value? (same counting type as your channel) " +
                   COLORS["Underline"] + COLORS["Bold"] + COLORS["BlueBright"])
if countType == "Base64":
  countLast = isBase64(countLast_)
elif countType == "Hexadecimal":
  countLast = isHex(countLast_)
elif countType == "letter":
  countLast = isLetter(countLast_)
elif countType == "number":
  countLast = isNumber(countLast_)
elif countType == "integer":
  countLast = isInteger(countLast_)
if (type(countLast) != int and type(countLast) != float):
  print(COLORS["Reset"] + COLORS["Red"] + "Wrong last count! Please use a {0} value".format(countType) + COLORS["Reset"] + "\n")
  exit()
# print(COLORS["Reset"] + COLORS["BlueBright"] + "'{0}' ({1}) has been selected as the last value.".format(countLast_, countLast) + COLORS["Reset"])
  
print(COLORS["Reset"] + "\n" + COLORS["YellowBright"] +
      "Starting in {0} mode, with {1} as increment, starting after {2}.".format(countType, countIncrement, countLast) + COLORS["Reset"])
print(COLORS["Reset"] + COLORS["YellowBright"] + "Pressing 'ENTER' will add your increment." + COLORS["Reset"])
print(COLORS["Reset"] + COLORS["YellowBright"] + "Pressing ARROW 'LEFT'/'RIGHT' will add/remove 1x your increment to the current number." + COLORS["Reset"])
print(COLORS["Reset"] + COLORS["YellowBright"] + "Pressing ARROW 'UP'/'DOWN' will add/remove 1 to the current number." + COLORS["Reset"])
print(COLORS["Reset"] + COLORS["Yellow"] + "Press 'ESC' to stop the program." + COLORS["Reset"] + "\n")

if countType == "number":
  countNext = countLast + (countIncrement/2)
else:
  countNext = countLast + 1

def copyAny(number):
  global countType
  global next
  
  if countType == "Base64":
    next = toBase64(number)
  elif countType == "Hexadecimal":
    next = toHex(number)
  elif countType == "letter":
    next = toLetter(number)
  elif countType == "number":
    next = toNumber(number)
  elif countType == "integer":
    next = toInteger(number)
  
  if next == False:
    print(COLORS["Reset"] + COLORS["Red"] + "An error occured on the copy." + COLORS["Reset"] + "\n")
    exit()
  
  pyperclip.copy(next)
  if pasteNext == True:
    controller = Keyboard.Controller()
    controller.press(Keyboard.Key.ctrl)
    controller.press('v')
    controller.release(Keyboard.Key.ctrl)
    controller.release('v')
    
  print(COLORS["Reset"] + COLORS["White"] + "Copied {0} (no. {1})".format(next, number) + COLORS["Reset"])

copyAny(countNext)

def on_press(key):
  global counted
  global removed
  global countIncrement
  global countNext
  
  if key == Keyboard.Key.esc:
    print(COLORS["Reset"] + "\n" + COLORS["Cyan"] + "Stopping the program..." + COLORS["Reset"])
    print(COLORS["Reset"] + COLORS["CyanBright"] + "You counted {0} times during this session.".format(counted) + COLORS["Reset"] + "\n")
    exit()
  
  elif key == Keyboard.Key.enter:
    counted += 1
    print(COLORS["Reset"] + COLORS["White"] + "Counted '{0}' ({1}). Counted {2} times this session.".format(countNext, next, counted) + COLORS["Reset"])
    countNext += countIncrement
    copyAny(countNext)
    
  elif key == Keyboard.Key.left:
    if counted >= 1:
      counted -= 1
      removed += 1
      print(COLORS["Reset"] + COLORS["White"] + "Removed a count to this session ({0} times counted).".format(counted) + COLORS["Reset"])
    countNext -= countIncrement
    copyAny(countNext)
  elif key == Keyboard.Key.right:
    if removed > 0:
      counted += 1
      removed -= 1
      print(COLORS["Reset"] + COLORS["White"] + "Added a count to this session ({0} times counted).".format(counted) + COLORS["Reset"])
    countNext += countIncrement
    copyAny(countNext)
  elif key == Keyboard.Key.up:
    countNext += 1
    copyAny(countNext)
  elif key == Keyboard.Key.down:
    countNext -= 1
    copyAny(countNext)
  
  # else:
  #   print("{0} pressed".format(key))
  
with Keyboard.Listener(on_press=on_press) as listener:
  listener.join()