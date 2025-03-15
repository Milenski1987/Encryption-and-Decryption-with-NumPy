import numpy as np
#import required library


def text_to_matrix(text, size):
#Function for converting text to matrix (ASCII codes)
    # Преобразува всеки символ в ASCII код и ги съхранява в списък
    text_as_code = [ord(character) for character in text]
    # Допълва списъка с нули, ако дължината не е кратна на размера на матрицата
    while len(text_as_code) % size != 0:
        text_as_code.append(0)
    # Преобразува списъка в NumPy матрица с размер size (брой колони)
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