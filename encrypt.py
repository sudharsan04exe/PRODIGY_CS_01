LETTERS = "abcdefghijklmnopqrstuvwxyz"

def encrypt(string, shift):
    encrypted_string = ""
    for i in string.lower():
        if i in LETTERS:
            encrypted_string += LETTERS[(LETTERS.index(i) + shift) % len(LETTERS)]
    return encrypted_string

# Get user input for message and shift value
string = input("Enter the message: ")
shift = int(input("Enter the shifting value: "))

# Print the encrypted result
print(encrypt(string, shift))

