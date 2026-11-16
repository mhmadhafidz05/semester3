def subset_sum(A, target):
    solusi = []

    def backtracking(i, total, subset, sisa):
        # Jika jumlah sesuai target
        if total == target:
            print("Solusi ditemukan:", subset)
            solusi.append(subset.copy())
            return

        # Pemangkasan cabang
        if total > target:
            print("Pangkas:", subset, "(melebihi target)")
            return

        if total + sisa < target:
            print("Pangkas:", subset, "(tidak cukup)")
            return

        if i == len(A):
            return

        # Pilihan 1: Ambil angka
        subset.append(A[i])
        backtracking(
            i + 1,
            total + A[i],
            subset,
            sisa - A[i]
        )

        # Backtracking: batalkan pilihan
        subset.pop()

        # Pilihan 2: Tidak ambil angka
        backtracking(
            i + 1,
            total,
            subset,
            sisa - A[i]
        )

    backtracking(0, 0, [], sum(A))
    return solusi


# Input pengguna
A = list(map(int, input(
    "Masukkan anggota himpunan A: "
).split()))

target = int(input("Masukkan nilai target: "))

# Proses
if any(x <= 0 for x in A) or target < 0:
    print("Gunakan angka positif dan target tidak negatif.")
else:
    print("\nProses Backtracking:")
    hasil = subset_sum(A, target)

    print("\nHasil Akhir:")
    if hasil:
        for i, subset in enumerate(hasil, 1):
            print(f"Solusi {i}: {subset}")
        print("Jumlah solusi:", len(hasil))
    else:
        print("Tidak ada solusi.")
