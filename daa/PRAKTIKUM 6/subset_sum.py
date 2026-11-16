def subset_sum(angka, target):
    solusi = []

    def backtrack(i, total, dipilih, sisa, spasi="", langkah="Mulai"):
        print(f"{spasi}{langkah}: total={total}, subset={dipilih}")

        # Jika jumlah sesuai target
        if total == target:
            print(f"{spasi}--> SOLUSI DITEMUKAN")
            solusi.append(dipilih.copy())
            return

        # Pangkas jika jumlah melebihi target
        if total > target:
            print(f"{spasi}--> PANGKAS (melebihi target)")
            return

        # Pangkas jika sisa angka tidak cukup
        if total + sisa < target:
            print(f"{spasi}--> PANGKAS (sisa tidak cukup)")
            return

        if i == len(angka):
            return

        nilai = angka[i]

        # Pilihan 1: Ambil angka
        dipilih.append(nilai)
        backtrack(
            i + 1, total + nilai, dipilih,
            sisa - nilai, spasi + "  ",
            f"Ambil {nilai}"
        )

        # Backtracking
        dipilih.pop()

        # Pilihan 2: Tidak ambil angka
        backtrack(
            i + 1, total, dipilih,
            sisa - nilai, spasi + "  ",
            f"Lewati {nilai}"
        )

    backtrack(0, 0, [], sum(angka))
    return solusi


# Input pengguna
angka = list(map(int, input(
    "Masukkan anggota A (pisahkan spasi): "
).split()))

target = int(input("Masukkan target: "))

# Proses
if any(x <= 0 for x in angka) or target < 0:
    print("Gunakan angka positif dan target tidak negatif.")
else:
    print("\nPohon Ruang Keadaan:")
    hasil = subset_sum(angka, target)

    print("\nHASIL AKHIR")
    if hasil:
        for i, subset in enumerate(hasil, 1):
            print(f"Solusi {i}: {subset} = {sum(subset)}")
        print("Jumlah solusi:", len(hasil))
    else:
        print("Tidak ditemukan solusi.")
