import base64

varLast = input("What was the last bese64? ")

print(varLast + " is equal to " + base64.b64decode(varLast).decode())