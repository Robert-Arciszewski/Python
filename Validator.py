userInput = input("Wpisz: ")

try:
   val = int(userInput)
except ValueError:
   print("That's not an int!")