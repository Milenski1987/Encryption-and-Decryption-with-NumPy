import numpy as np
from random import randint
#import required library


def text_to_matrix(text, size):
#Function for converting text to matrix (ASCII codes)
    # Converts each character to ASCII code and stores them in a list
    text_as_code = [ord(character) for character in text]
    # Appends zeros to list if the length is not a multiple of the matrix size
    while len(text_as_code) % size != 0:
        text_as_code.append(0)
    # Converts the list to a NumPy matrix of size (number of columns)
    text_as_code = np.array(text_as_code)
    text_as_code = text_as_code.reshape(len(text_as_code) // 2, 2)
    return text_as_code

def generate_key():
# Generate random key for better security
    # Generate random key matrix
    key_matrix = np.random.rand(2, 2)
    return key_matrix

def encrypt(matrix, key):
# Key matrix multiplication encryption function
    # Using np.dot() to multiply the matrix by the key
    encrypted_matrix = np.dot(matrix, key)
    return encrypted_matrix

def decrypt(encrypted_matrix, key):
# Decryption function via inverse matrix
    # Finding the inverse matrix with np.linalg.inv()
    inverted_key = np.linalg.inv(key)
    # Using np.dot() to multiply with the inverse matrix
    decrypted_matrix = np.dot(encrypted_matrix, inverted_key)
    # Converts the result to integers
    decrypted_matrix = np.round(decrypted_matrix).astype(int)
    return decrypted_matrix

def matrix_to_text(matrix):
# Function to convert a matrix back to text
    # Converts the matrix to a one-dimensional list
    text_as_code = [number for row in matrix for  number in row if number != 0]
    # Converts ASCII codes back to characters
    text = ""
    for number in text_as_code:
        text += chr(number)
    return text


# --- Program demonstration ---
# Input text for encryption
text = input("Enter your message: ")
print(f"Original message: {text}")

# Define a key matrix (must be invertible)
key = generate_key()

# Convert text to a numeric matrix
matrix = text_to_matrix(text, 2)
print("Original matrix:\n", matrix)

# Matrix encryption
encrypted_matrix = encrypt(matrix, key)
print("Encrypted matrix:\n", encrypted_matrix)

# Matrix decryption
decrypted_matrix = decrypt(encrypted_matrix, key)
print("Decrypted matrix:\n", decrypted_matrix)

# Convert back to text
decrypted_text = matrix_to_text(decrypted_matrix)
print("Deciphered text:", decrypted_text)