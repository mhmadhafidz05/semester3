n = int(input("Masukkan nilai n (pangkat 2): "))
x = int(input("Masukkan nilai x: "))

j = n
operasi = 0

while j >= 1:
    for i in range(1, j + 1):
        x = x * i
        operasi += 1

    j = j // 2

jumlah = x

print("\nHasil perkalian =", jumlah)
print("Jumlah operasi perkalian =", operasi)

print("\nAnalisis Kompleksitas:")
print("T(n) = n + n/2 + n/4 + ... + 2 + 1")
print("T(n) = 2n - 1")
print(f"T({n}) = {2 * n - 1}")

print("\nKompleksitas Asimptotik:")
print("T(n) = 2n - 1")
print("Suku dominan = n")
print("Kompleksitas waktu = O(n)")