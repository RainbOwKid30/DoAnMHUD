import tkinter as tk
from tkinter import messagebox

def generate_playfair_matrix(key):
    key = "".join(dict.fromkeys(key.replace(" ", "")))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []

    for char in key:
        if char not in matrix:
            matrix.append(char)

    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    return matrix

def preprocess_plaintext(plaintext):
    plaintext = plaintext.replace(" ", "").replace("J", "I")
    pairs = [plaintext[i:i + 2] for i in range(0, len(plaintext), 2)]
    for i in range(len(pairs)):
        if len(pairs[i]) == 1:
            pairs[i] += 'X'
    return pairs

def encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    pairs = preprocess_plaintext(plaintext)
    ciphertext = ""

    for pair in pairs:
        row1, col1 = divmod(matrix.index(pair[0]), 5)
        row2, col2 = divmod(matrix.index(pair[1]), 5)

        if row1 == row2:
            ciphertext += matrix[row1 * 5 + (col1 + 1) % 5]
            ciphertext += matrix[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[((row1 + 1) % 5) * 5 + col1]
            ciphertext += matrix[((row2 + 1) % 5) * 5 + col2]
        else:
            ciphertext += matrix[row1 * 5 + col2]
            ciphertext += matrix[row2 * 5 + col1]

    return ciphertext

def decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    pairs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    plaintext = ""

    for pair in pairs:
        row1, col1 = divmod(matrix.index(pair[0]), 5)
        row2, col2 = divmod(matrix.index(pair[1]), 5)

        if row1 == row2:
            plaintext += matrix[row1 * 5 + (col1 - 1) % 5]
            plaintext += matrix[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[((row1 - 1) % 5) * 5 + col1]
            plaintext += matrix[((row2 - 1) % 5) * 5 + col2]
        else:
            plaintext += matrix[row1 * 5 + col2]
            plaintext += matrix[row2 * 5 + col1]

    return plaintext

def on_encrypt_button_click():
    key = key_entry.get().upper()
    plaintext = plaintext_entry.get().upper()
    encrypted_text = encrypt(plaintext, key)
    encrypted_text_var.set(encrypted_text)

def on_decrypt_button_click():
    key = key_entry.get().upper()
    ciphertext = ciphertext_entry.get().upper()
    decrypted_text = decrypt(ciphertext, key)
    decrypted_text_var.set(decrypted_text)

# Tạo cửa sổ chương trình
window = tk.Tk()
window.title("Playfair")

# Khung nhập key
key_label = tk.Label(window, text="Key (loại bỏ trùng lặp và khoảng trắng):")
key_label.pack()
key_entry = tk.Entry(window)
key_entry.pack()

# Khung nhập văn bản
plaintext_label = tk.Label(window, text="Văn bản:")
plaintext_label.pack()
plaintext_entry = tk.Entry(window)
plaintext_entry.pack()

# Nút mã hóa
encrypt_button = tk.Button(window, text="Mã hóa", command=on_encrypt_button_click)
encrypt_button.pack()

# Khung hiển thị văn bản đã mã hóa
encrypted_text_var = tk.StringVar()
encrypted_text_label = tk.Label(window, textvariable=encrypted_text_var)
encrypted_text_label.pack()

# Khung nhập văn bản đã mã hóa
ciphertext_label = tk.Label(window, text="Văn bản đã mã hóa:")
ciphertext_label.pack()
ciphertext_entry = tk.Entry(window)
ciphertext_entry.pack()

# Nút giải mã
decrypt_button = tk.Button(window, text="Giải mã", command=on_decrypt_button_click)
decrypt_button.pack()

# Khung hiển thị văn bản đã giải mã
decrypted_text_var = tk.StringVar()
decrypted_text_label = tk.Label(window, textvariable=decrypted_text_var)
decrypted_text_label.pack()

window.mainloop()
