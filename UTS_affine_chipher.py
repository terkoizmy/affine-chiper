import math

# Fungsi untuk mencari invers modular
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Fungsi untuk enkripsi menggunakan Affine Cipher
def affine_encrypt(plaintext, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("a dan 26 harus coprime (relatif prima).")
    ciphertext = ''
    for char in plaintext.upper():
        if char.isalpha():
            x = ord(char) - ord('A')
            y = (a * x + b) % 26
            ciphertext += chr(y + ord('A'))
        else:
            ciphertext += char
    return ciphertext

# Fungsi untuk dekripsi menggunakan Affine Cipher
def affine_decrypt(ciphertext, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("a dan 26 harus coprime (relatif prima).")
    plaintext = ''
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Tidak ada invers modular untuk a.")
    for char in ciphertext.upper():
        if char.isalpha():
            y = ord(char) - ord('A')
            x = (a_inv * (y - b)) % 26
            plaintext += chr(x + ord('A'))
        else:
            plaintext += char
    return plaintext

# Fungsi untuk melakukan kriptoanalisis pada ciphertext yang diberikan.
def affine_cryptanalysis(ciphertext):
    possible_plaintexts = []
    for a in range(1, 26):
        if math.gcd(a, 26) == 1:  # Hanya gunakan nilai a yang relatif prima dengan 26
            for b in range(26):
                try:
                    decrypted_text = affine_decrypt(ciphertext, a, b)
                    possible_plaintexts.append((a, b, decrypted_text))
                except ValueError:
                    continue
    return possible_plaintexts

# Cara Pemakaian
plaintext = "UTS Susah banget"
a = 15 # Slope
b = 2 # Intercept

print("Plaintext:", plaintext)
ciphertext = affine_encrypt(plaintext, a, b)
print("Ciphertext:", ciphertext)
decrypted_text = affine_decrypt(ciphertext, a, b)
print("Decrypted Text:", decrypted_text)

print("Ciphertext:", ciphertext)
results = affine_cryptanalysis(ciphertext)

print("Analisis :")
for a, b, decrypted_text in results:
  print(f"a = {a}, b = {b}, Plaintext = {decrypted_text}")
  if decrypted_text == plaintext.upper():
    print("slopenya adalah: ", a ,  " dan interceptnya adalah: ", b)
    break

