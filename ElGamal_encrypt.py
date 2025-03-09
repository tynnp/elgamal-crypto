import os
from ElGamal_algorithm import generate_keys, encrypt

input_file = input("Nhập đường dẫn file cần mã hóa: ").strip()
base, ext = os.path.splitext(input_file)

with open(input_file, 'rb') as f:
    plaintext = f.read()

plaintext_file = "plaintext.txt"
with open(plaintext_file, 'w') as f:
    f.write(" ".join(map(str, plaintext)))
print(f"Bản rõ đã được lưu tại: {plaintext_file}")

p, alpha, beta, a = generate_keys(min_prime=10000, max_prime=70000)

# In thông tin khóa
print("-" * 100)
print("Thông tin mã hóa:")
print(f"p = {p}")
print(f"alpha = {alpha}")
print(f"beta = {beta}")
print(f"a = {a}")
print(f"-> Khóa công khai: ({p}, {alpha}, {beta})")
print(f"-> Khóa bí mật: ({a})")

info = {
    "p": p,
    "alpha": alpha,
    "beta": beta,
    "a": a,
    "ext": ext
}

with open("info.txt", 'w') as f:
    for k, v in info.items():
        f.write(f"{k}:{v}\n")
print("Thông tin khóa và phần mở rộng file được lưu tại info.txt")

# Thực hiện mã hóa
plaintext = list(plaintext)
ciphertext = encrypt(plaintext, p, alpha, beta)

# Lưu ciphertext ra file 
ciphertext_file = "ciphertext.txt"
with open(ciphertext_file, 'w') as f:
    f.write(" ".join(map(str, ciphertext)))
print(f"Bản mã đã được lưu tại: {ciphertext_file}")
print("-" * 100)