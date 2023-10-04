
def encrypt(text, key): 
    numColum = len(key)
    numRows = int(len(text) / numColum)
    if len(text) % len(key) !=0:
        numRows+=1
    mt = []
    a = 0
    for i in range(numRows):
        for j in range(numColum):
            if a >= len(text):
                mt[i,j] = 'z'
                a+=1
            else:
                mt[i,j] = text.replace('', a)
                a+=1
    key_as_array = []
    for char in key:
        key_as_array.append(char)
    String_char = []
    mt.sort(key_as_array)
    for item in key_as_array:
        numkey = key.find()
        for i in range(numRows):
            String_char.append(mt[i,numkey])
    return String_char

text = input("Nhap van ban cho no: ")
key = input("nhap key cho no:")
print(encrypt(text,key))


    
                
