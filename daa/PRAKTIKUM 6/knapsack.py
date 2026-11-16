def knapsack(berat, nilai, kapasitas):
    n = len(berat)

    # Inisialisasi tabel DP
    F = [[0] * (kapasitas + 1) for _ in range(n + 1)]

    # Proses Dynamic Programming
    for i in range(1, n + 1):
        for j in range(kapasitas + 1):
            if berat[i - 1] <= j:
                F[i][j] = max(
                    F[i - 1][j],
                    nilai[i - 1] + F[i - 1][j - berat[i - 1]]
                )
            else:
                F[i][j] = F[i - 1][j]

    # Penelusuran barang yang dipilih
    hasil = []
    j = kapasitas

    for i in range(n, 0, -1):
        if F[i][j] != F[i - 1][j]:
            hasil.append(i)
            j -= berat[i - 1]

    hasil.reverse()
    return F, hasil


# Input pengguna
n = int(input("Masukkan jumlah barang: "))
kapasitas = int(input("Masukkan kapasitas tas: "))

berat = []
nilai = []

for i in range(n):
    print(f"\nBarang ke-{i + 1}")
    w = int(input("Masukkan berat barang: "))
    v = int(input("Masukkan nilai barang: "))

    berat.append(w)
    nilai.append(v)

# Proses
F, hasil = knapsack(berat, nilai, kapasitas)

# Tampilkan tabel
print("\nTabel Dynamic Programming")
print("i\\j", *range(kapasitas + 1), sep="\t")

for i in range(n + 1):
    print(i, *F[i], sep="\t")

# Hasil akhir
print("\nBarang yang dipilih:", hasil)
print("Nilai maksimum:", F[n][kapasitas])

total_berat = sum(berat[i - 1] for i in hasil)
print("Total berat:", total_berat)

