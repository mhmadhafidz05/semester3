def coin_change(koin, n):
    # Inisialisasi tabel DP
    F = [float('inf')] * (n + 1)
    F[0] = 0

    # Menyimpan koin yang dipilih
    pilihan = [-1] * (n + 1)

    # Proses Dynamic Programming
    for i in range(1, n + 1):
        for d in koin:
            if d <= i and F[i - d] + 1 < F[i]:
                F[i] = F[i - d] + 1
                pilihan[i] = d

    # Penelusuran koin yang digunakan
    hasil = []
    sisa = n

    if F[n] == float('inf'):
        return F, hasil

    while sisa > 0:
        d = pilihan[sisa]
        hasil.append(d)
        sisa -= d

    return F, hasil


# Input pengguna
jumlah = int(input("Masukkan jumlah jenis koin: "))

koin = []
for i in range(jumlah):
    nilai = int(input(f"Masukkan nilai koin ke-{i+1}: "))
    koin.append(nilai)

n = int(input("Masukkan nilai yang ingin ditukar: "))

# Proses
F, hasil = coin_change(koin, n)

print("\nTabel Dynamic Programming")
print("n\t:", *range(n + 1), sep="\t")
print("F(n)\t:", *F, sep="\t")

if F[n] != float('inf'):
    print("\nKoin yang digunakan:", hasil)
    print("Jumlah koin minimum:", F[n])
else:
    print("\nNilai tidak dapat ditukar.")
