from pynput import keyboard
import pyperclip
import base64

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

print("Press ESC to leave the programm.")
controller = keyboard.Controller()

def on_press(key):
  global varNumber, varType
  try:
    if key == keyboard.Key.enter:
      
      if varType == "base64":
        varB64 = base64.b64encode(str(varNumber).encode()).decode()
        pyperclip.copy(varB64)
      else:
        pyperclip.copy(str(varNumber))
      
      with controller.pressed(keyboard.Key.ctrl):
        controller.press('v')
        controller.release('v')
  
      if varType == "normal" or varType == "base64":
        varNumber += 2
      elif varType == "backwards":
        varNumber -= 2
          
    # Stop
    elif key == keyboard.Key.esc:
      print("Leaving programm.")
      return False

  except AttributeError:
    pass

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
  listener.join()