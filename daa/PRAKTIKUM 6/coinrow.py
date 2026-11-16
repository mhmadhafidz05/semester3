def coin_row(koin):
    n = len(koin)

    F = [0] * (n + 1)

    if n == 0:
        return 0, []

    F[1] = koin[0]

    # Menghitung nilai maksimum
    for i in range(2, n + 1):
        F[i] = max(
            koin[i - 1] + F[i - 2],
            F[i - 1]
        )

    # Menelusuri koin yang diambil
    hasil = []
    i = n

    while i >= 1:
        if i == 1:
            if F[i] > 0:
                hasil.append(koin[0])
            break

        if koin[i - 1] + F[i - 2] > F[i - 1]:
            hasil.append(koin[i - 1])
            i -= 2
        else:
            i -= 1

    hasil.reverse()
    return F, hasil


# Input pengguna
n = int(input("Masukkan jumlah koin: "))

koin = []
for i in range(n):
    nilai = int(input(f"Masukkan nilai koin ke-{i+1}: "))
    koin.append(nilai)

# Proses
if n > 0:
    F, hasil = coin_row(koin)

    print("\nTabel Dynamic Programming")
    print("i\t:", *range(n + 1), sep="\t")
    print("F(i)\t:", *F, sep="\t")

    print("\nKoin yang diambil:", hasil)
    print("Jumlah maksimum:", F[n])
else:
    print("Jumlah maksimum: 0")
