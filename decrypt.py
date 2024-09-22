LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(string, shift):
 
  lower_string = string.lower()
  decrypted_string = ""

  for char in lower_string:
    if char in LETTERS:
      decrypted_string += LETTERS[(LETTERS.index(char) - shift) % len(LETTERS)]

  return decrypted_string


# Get user input for message and shift value
string = input("Enter the message: ")
shift = int(input("Enter the shifting value: "))

# Print the encrypted result
print(decrypt(string, shift))
