from pynput import keyboard
import pyperclip
import base64

print("")

# The counting channel type
varChannel = input("Choose your channel between 'counting' (1), 'backwards' (2), 'base64' (3): ")
if varChannel == "1" or varChannel == "counting":
  varType = "normal"
elif varChannel == "2" or varChannel == "backwards":
  varType = "backwards"
elif varChannel == "3" or varChannel == "base64":
  varType = "base64"
else:
  raise Exception("Must choose between 1, 2 or 3.")

# The next number to send
varLast = input("Enter the last number: ")
if varType == "normal" or varType == "base64":
  varNumber = int(varLast) + 1
elif varType == "backwards":
  varNumber = int(varLast) - 1
else:
  raise Exception("Unknown channel.")

# Every how much to count
varEach = int(input("all how many numbers do you want to count: "))

needCtrlV = True
print("")
if needCtrlV == True:
  print("Press CTRL + V to paste number")
print("Press 'TAB' to recover your last number sent.")
print("Press 'ESC' to leave the programm.")
print("")

controller = keyboard.Controller()

def prepare_next():
  global varType
  if varType == "base64":
    varB64 = base64.b64encode(str(varNumber).encode()).decode()
    pyperclip.copy(varB64)
  else:
    pyperclip.copy(str(varNumber))
    
  if needCtrlV == True:
    with controller.pressed(keyboard.Key.ctrl):
      controller.press('v')
      controller.release('v')
    
def on_press(key):
  global varType, varNumber
  try:
    if key == keyboard.Key.enter:
      print("copied: " + str(varNumber))
      prepare_next()
      if varType == "normal" or varType == "base64":
        varNumber += varEach
      elif varType == "backwards":
        varNumber -= varEach
    
    elif key == keyboard.Key.tab:
      print("next: " + str(varNumber))
      if varType == "normal" or varType == "base64":
        varNumber -= varEach+1
      elif varType == "backwards":
        varNumber += varEach+1
      print("copied: " + str(varNumber))
      prepare_next()
      if varType == "normal" or varType == "base64":
        varNumber += varEach
      elif varType == "backwards":
        varNumber -= varEach
          
    # Stop
    elif key == keyboard.Key.esc:
      print("\nLeaving programm.\n")
      return False

  except AttributeError:
    pass

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
  listener.join()