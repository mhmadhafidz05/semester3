
def brute_force(T, P):
    n = len(T)
    m = len(P)
    perbandingan = 0

    for i in range(n - m + 1):
        j = 0

        while j < m:
            perbandingan += 1

            if T[i + j] != P[j]:
                break

            j += 1

        if j == m:
            return i, perbandingan

    return -1, perbandingan


# Latihan 7 Nomor 1
T = "THERE_IS_MORE_TO_LIFE_THAN_INCREASING_ITS_SPEED"
P = "GANDHI"

posisi, jumlah = brute_force(T, P)

print("=== LATIHAN 7 NOMOR 1 ===")
print("Panjang teks (n):", len(T))
print("Panjang pola (m):", len(P))
print("Jumlah perbandingan:", jumlah)
print("Posisi pola:", posisi)
print("Pola ditemukan" if posisi != -1 else "Pola tidak ditemukan")

# Latihan 7 Nomor 2 (Worst Case)
T = "BELAJAR_BELAJAR_BELAJAR"
P = "BELAJAR_BELAJAS"

posisi, jumlah = brute_force(T, P)

print("\n=== LATIHAN 7 NOMOR 2 ===")
print("Teks:", T)
print("Pola:", P)
print("Panjang teks (n):", len(T))
print("Panjang pola (m):", len(P))
print("Jumlah perbandingan:", jumlah)
print("Worst Case: O(n * m)")