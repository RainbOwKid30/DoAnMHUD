import tkinter as tk

# Hàm để mã hóa hoặc giải mã văn bản sử dụng Ceasar Cipher
def ceasar_cipher(text, shift, mode):
    result = ""
    for char in text:
        # isalpha trả về giá trị true 
        # nếu chuỗi có ít nhất 1 ký tự và tất cả các ký tự đó đều là chữ cái
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            # cái mode này tức là để khi tui ấn nút encrypt(mã hóa)
            #  thì nó sẽ vô nó tính toán dòng shifted
            # ngược lại bấm decrypt(giải mã) sẽ tính toán dòng else
            if mode == "encrypt":
                # ord trả về Unicode cho 1 ký tự
                shifted = (ord(char) - ord('a') + shift) % 26
            else:
                shifted = (ord(char) - ord('a') - shift) % 26
                # chr biến số nguyên thành ký tự unicode tương đương với nó.
            shifted_char = chr(ord('a') + shifted)
            if is_upper:
                shifted_char = shifted_char.upper()
            # result : đây là cái chuỗi để lưu trữ
            result += shifted_char
        else:
            result += char
    return result

# Hàm xử lý sự kiện khi người dùng nhấn nút "Mã hóa"
def encrypt_text():
    input_text = input_entry.get()
    shift_value = int(shift_entry.get())
    encrypted_text = ceasar_cipher(input_text, shift_value, "encrypt")
    output_label.config(text="Kết quả mã hóa: " + encrypted_text)

# Hàm xử lý sự kiện khi người dùng nhấn nút "Giải mã"
def decrypt_text():
    input_text = input_entry.get()
    shift_value = int(shift_entry.get())
    decrypted_text = ceasar_cipher(input_text, shift_value, "decrypt")
    output_label.config(text="Kết quả giải mã: " + decrypted_text)

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Ceasar Cipher")

# Tạo và định dạng các thành phần trên giao diện
input_label = tk.Label(window, text="Nhập văn bản:")
input_label.pack(pady=10)
input_entry = tk.Entry(window)
input_entry.pack(pady=5)

shift_label = tk.Label(window, text="Nhập key:")
shift_label.pack()
shift_entry = tk.Entry(window)
shift_entry.pack(pady=5)

encrypt_button = tk.Button(window, text="Mã hóa", command=encrypt_text)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(window, text="Giải mã", command=decrypt_text)
decrypt_button.pack(pady=5)

output_label = tk.Label(window, text="", wraplength=300)
output_label.pack()

# Chạy ứng dụng
window.mainloop()