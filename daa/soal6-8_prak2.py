n = int(input("Masukkan nilai n (pangkat 2): "))
x = int(input("Masukkan nilai x: "))

# =========================
# NOMOR 6
# =========================

j = n
operasi = 0

while j >= 1:
    for i in range(1, j + 1):
        x = x * i
        operasi = operasi + 1

    j = j // 2

jumlah = x

print("\n=========================")
print("HASIL NOMOR 6")
print("=========================")

print("Hasil perkalian =", jumlah)
print("Jumlah operasi perkalian =", operasi)

print("\nAnalisis Kompleksitas:")
print("T(n) = n + n/2 + n/4 + ... + 2 + 1")
print("T(n) = 2n - 1")

print(f"T({n}) = 2({n}) - 1")
print(f"T({n}) = {2 * n - 1}")

print("\nKompleksitas Asimptotik:")
print("T(n) = 2n - 1")
print("Suku dominan = n")
print("Kompleksitas waktu = O(n)")


# =========================
# NOMOR 7
# =========================

print("\n=========================")
print("PEMBUKTIAN NOMOR 7")
print("=========================")

T7 = 2 * n**2 + 6 * n + 1
C7 = 9
batas7 = C7 * n**2

print("T(n) = 2n^2 + 6n + 1")

print(f"\nT({n}) = 2({n})^2 + 6({n}) + 1")
print(f"T({n}) = {T7}")

print("\nPembuktian:")
print("2n^2 + 6n + 1 <= 9n^2")
print("C = 9")
print("n0 = 1")

print(f"\nT({n}) = {T7}")
print(f"9({n})^2 = {batas7}")

if n >= 1 and T7 <= batas7:
    print(f"{T7} <= {batas7}")
    print("Terbukti T(n) = O(n^2)")
else:
    print("Belum memenuhi pembuktian")

print("Kompleksitas waktu = O(n^2)")


# =========================
# NOMOR 8
# =========================

print("\n=========================")
print("PEMBUKTIAN NOMOR 8")
print("=========================")

T8 = 3 * n + 2
C8 = 5
batas8 = C8 * n

print("T(n) = 3n + 2")

print(f"\nT({n}) = 3({n}) + 2")
print(f"T({n}) = {T8}")

print("\nPembuktian:")
print("3n + 2 <= 3n + 2n")
print("3n + 2 <= 5n")
print("C = 5")
print("n0 = 1")

print(f"\nT({n}) = {T8}")
print(f"5({n}) = {batas8}")

if n >= 1 and T8 <= batas8:
    print(f"{T8} <= {batas8}")
    print("Terbukti T(n) = O(n)")
else:
    print("Belum memenuhi pembuktian")

print("Kompleksitas waktu = O(n)")