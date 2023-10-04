import random
import tkinter as tk

class BangMaChuDon:
    # khởi tạo giá trị 
    def __init__(self, key):
        self.key = key
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # hàm mã hóa
    def encrypt(self, plaintext):
        # plaintext này dùng để lưu chuỗi nhập vào và cho tất cả thành viết thường
        plaintext = plaintext.lower()
        # tạo 1 list rỗng
        ciphertext = ''
        for char in plaintext:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                ciphertext += self.key[index]
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        for char in ciphertext:
            if char in self.key:
                index = self.key.index(char)
                plaintext += self.alphabet[index]
            else:
                plaintext += char
        return plaintext

def generate_random_key():
    alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(alphabet_list)
    return ''.join(alphabet_list)

def encrypt_text():
    plaintext = plaintext_entry.get().lower()
    encrypted_text = cipher.encrypt(plaintext)
    encrypted_text_label.config(text=f'Encrypted: {encrypted_text}')

def decrypt_text():
    ciphertext = ciphertext_entry.get().lower()
    decrypted_text = cipher.decrypt(ciphertext)
    decrypted_text_label.config(text=f'Decrypted: {decrypted_text}')

def generate_new_random_key():
    global cipher
    random_key = generate_random_key()
    cipher = BangMaChuDon(random_key)
    random_key_label.config(text=f'Random Key: {random_key}')

# Khởi tạo giao diện người dùng
root = tk.Tk()
root.title("Bang Ma Chu Don")

# Tạo bảng mã chữ đơn với khóa ngẫu nhiên
random_key = generate_random_key()
cipher = BangMaChuDon(random_key)

# Tạo và định cấu hình các phần tử giao diện người dùng
plaintext_label = tk.Label(root, text="Plaintext:")
plaintext_label.pack()
plaintext_entry = tk.Entry(root)
plaintext_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack()

ciphertext_label = tk.Label(root, text="Ciphertext:")
ciphertext_label.pack()
ciphertext_entry = tk.Entry(root)
ciphertext_entry.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.pack()

random_key_button = tk.Button(root, text="Random Key", command=generate_new_random_key)
random_key_button.pack()

random_key_label = tk.Label(root, text=f'Random Key: {random_key}')
random_key_label.pack()

encrypted_text_label = tk.Label(root, text="")
encrypted_text_label.pack()

decrypted_text_label = tk.Label(root, text="")
decrypted_text_label.pack()

root.mainloop()
