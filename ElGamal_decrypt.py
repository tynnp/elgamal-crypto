from ElGamal_algorithm import *

ciphertext_file = "ciphertext.txt"
with open(ciphertext_file, 'r') as f:
    data = f.read().strip()
ciphertext = list(map(int, data.split()))

info = {}
with open("info.txt", 'r') as f:
    for line in f:
        if line.strip():
            k, v = line.split(':')
            info[k.strip()] = v.strip()

p = int(info["p"])
a = int(info["a"])
ext = info["ext"]

decrypted = decrypt(ciphertext, p, a)
decrypted_data = bytes(decrypted)

decrypted_file = "decrypted" + ext
with open(decrypted_file, 'wb') as f:
    f.write(decrypted_data)
print(f"File đã giải mã đã được lưu tại: {decrypted_file}")