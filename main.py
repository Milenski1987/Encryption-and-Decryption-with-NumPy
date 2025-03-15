import numpy as np
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


def encrypt(matrix, key):
# Key matrix multiplication encryption function
    # Използвай np.dot() за умножение на матрицата с ключа

    return encrypted_matrix

def decrypt(encrypted_matrix, key):
# Decryption function via inverse matrix
    # Намиране на обратната матрица с np.linalg.inv()

    # Използвай np.dot() за умножение с обратната матрица

    # Преобразува резултата в цели числа

    return decrypted_matrix

def matrix_to_text(matrix):
# Function to convert a matrix back to text
    # Преобразува матрицата в едномерен списък

    # Преобразува ASCII кодовете обратно в символи

    return text


# --- Program demonstration ---
# Input text for encryption
text = "HELLO"

# Define a key matrix (must be invertible)
key = np.array([[3, 2], [1, 4]])

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