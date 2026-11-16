n = int(input("Masukkan nilai n (pangkat 2): "))
x = int(input("Masukkan nilai x: "))

j = n
operasi = 0

while j >= 1:
    for i in range(1, j + 1):
        x = x * i
        operasi = operasi + 1

    j = j // 2

jumlah = x

T_n = 2 * n - 1

print("\nHasil perkalian =", jumlah)

print("\nJumlah Operasi:")
print("Operasi perkalian aktual =", operasi)

print("\nRumus Kompleksitas Waktu:")
print("T(n) = n + n/2 + n/4 + ... + 2 + 1")
print("T(n) = 2n - 1")

print(f"\nT({n}) = 2({n}) - 1")
print(f"T({n}) = {T_n}")

print("\nKompleksitas Waktu:")
print("T(n) = 2n - 1")
print("Kompleksitas waktu = O(n)")