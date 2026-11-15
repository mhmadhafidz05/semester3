def brute_force_string_match(T, P):
    n = len(T)
    m = len(P)
    perbandingan = 0

    if m == 0:
        return 0, perbandingan

    for i in range(n - m + 1):
        j = 0

        while j < m:
            perbandingan += 1

            if P[j] != T[i + j]:
                break

            j += 1

        if j == m:
            return i, perbandingan

    return -1, perbandingan


# Input teks dan pola
T = input("Masukkan teks (T): ")
P = input("Masukkan pola (P): ")

# Proses pencarian
posisi, perbandingan = brute_force_string_match(T, P)

print("\n=== HASIL PENCOCOKAN STRING ===")
print("Teks:", T)
print("Pola:", P)
print("Panjang teks (n):", len(T))
print("Panjang pola (m):", len(P))

if posisi != -1:
    print("Pola ditemukan!")
    print("Indeks ke-", posisi)
    print("Posisi karakter ke-", posisi + 1)
else:
    print("Pola tidak ditemukan!")

print("\n=== ANALISIS KOMPLEKSITAS ===")
print("Jumlah perbandingan:", perbandingan)
print("Worst Case: O(n * m)")
print("Space Complexity: O(1)")
