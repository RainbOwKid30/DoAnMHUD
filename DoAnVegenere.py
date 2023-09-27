import tkinter as tk
# def giống là cú pháp để tạo ra tên biến để có gì xuống dưới nó có thể lấy dùng lại 
# nó giống như mình tạo ra 1 cái hàm để khi muốn tính toán thì nó sẽ trỏ đến hàm này.
def vigenere_encrypt(plain_text, key):
    # tạo 1 list rỗng
    encrypted_text = []
    #lấy độ dài của key mình đưa vào
    key_length = len(key)
    
    # chạy từng vị trí theo độ dài chuỗi
    for i in range(len(plain_text)):
        # lưu giá trị  tại vị trí đó vào char
        char = plain_text[i]
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            # khi làm xong thuật toán nó sẽ thêm vào list ban đầu khởi tạo
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    # khi làm xong các bước trên nó sẽ lưu vào list encrypted_text
    return ''.join(encrypted_text)

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = []
    key_length = len(key)
    
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        # isalpha trả về giá trị true 
        # nếu chuỗi có ít nhất 1 ký tự và tất cả các ký tự đó đều là chữ cái
        if char.isalpha():
            # ord trả về Unicode cho 1 ký tự
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.islower():
                # chr biến số nguyên thành ký tự unicode tương đương với nó.
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)
# dùng để tạo nút bấm cho chương trình chạy khi có các dữ liệu được nhập vào.
def encrypt_button_click():
    plain_text = plain_text_entry.get()
    key = key_entry.get()
    encrypted_text = vigenere_encrypt(plain_text, key)
    encrypted_text_label.config(text="Encrypted Text: " + encrypted_text)

def decrypt_button_click():
    encrypted_text = encrypted_text_entry.get()
    key = key_entry.get()
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    decrypted_text_label.config(text="Decrypted Text: " + decrypted_text)

# Tạo cửa sổ
window = tk.Tk()
window.title("Vigenere")

# Tạo các widget
plain_text_label = tk.Label(window, text="Enter Plain Text:")
plain_text_entry = tk.Entry(window)
key_label = tk.Label(window, text="Enter Key:")
key_entry = tk.Entry(window)
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_button_click)
encrypted_text_label = tk.Label(window, text="Encrypted Text: ")
encrypted_text_entry = tk.Entry(window)
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_button_click)
decrypted_text_label = tk.Label(window, text="Decrypted Text: ")

# Đặt các widget vào cửa sổ
plain_text_label.pack()
plain_text_entry.pack()
key_label.pack()
key_entry.pack()
encrypt_button.pack()
encrypted_text_label.pack()
encrypted_text_entry.pack()
decrypt_button.pack()
decrypted_text_label.pack()

# Chạy ứng dụng
window.mainloop()
