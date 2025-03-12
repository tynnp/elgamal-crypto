from ElGamal_algorithm import *

# Nhập giới hạn số nguyên tố được sinh
print("-" * 100)
min_prime = int(input("Nhập giới hạn nhỏ nhất của số nguyên tố: "))
max_prime = int(input("Nhập giới hạn lớn nhất của số nguyên tố: "))

# Sinh khóa công khai và khóa bí mật
p, alpha, beta, a = generate_keys(min_prime, max_prime)
public_key = {"p": p, "alpha": alpha, "beta": beta}
private_key = {"p": p, "a": a}

# In thông tin khóa 
print("Thông tin mã hóa:")
print(f"p = {p}")
print(f"alpha = {alpha}")
print(f"beta = {beta}")
print(f"a = {a}")
print(f"-> Khóa công khai (p, alpha, beta): ({p}, {alpha}, {beta})")
print(f"-> Khóa bí mật (p, a): ({p}, {a})")

# Lưu khóa bí mật
priv_file = "private_key.json"
with open(priv_file, "w") as f:
    json.dump(private_key, f, indent=4)
print(f"Khóa bí mật được lưu tại {priv_file}")

# Lưu khóa công khai
pub_file = "public_key.json"
with open(pub_file, "w") as f:
    json.dump(public_key, f, indent=4)
print(f"Khóa công khai được lưu tại {pub_file}", "-" * 100, sep='\n')