# Caesar Cipher Program

This repository contains a simple Python implementation of the Caesar Cipher encryption and decryption algorithm.

## About

The Caesar Cipher is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down or up the alphabet. This program supports both encryption and decryption using a user-defined shift value.

## Features

- **Encrypt a message** using the Caesar Cipher.
- **Decrypt a message** that was encrypted with the Caesar Cipher.

## How It Works

1. **Encryption**: Each letter in the plaintext is shifted by a certain number of positions (the "shift" value) in the alphabet.
2. **Decryption**: The reverse process is used to retrieve the original message by shifting each letter back by the same value.

### Encryption Process

- For each character in the input string:
  - If the character is a letter, find its index in the alphabet.
  - Add the shift value to the index and apply modulo to wrap around if necessary.
  - Replace the character with the letter at the new index.

### Decryption Process

- Similar to encryption, but subtract the shift value from the index.

## Example

### Encrypting a Message

To encrypt the message "hello" with a shift of 3:

- 'h' → 'k' (h + 3)
- 'e' → 'h' (e + 3)
- 'l' → 'o' (l + 3)
- 'l' → 'o' (l + 3)
- 'o' → 'r' (o + 3)

**Encrypted Message**: "khoor"

### Decrypting a Message

To decrypt the message "khoor" with a shift of 3:

- 'k' → 'h' (k - 3)
- 'h' → 'e' (h - 3)
- 'o' → 'l' (o - 3)
- 'o' → 'l' (o - 3)
- 'r' → 'o' (r - 3)

**Decrypted Message**: "hello"

