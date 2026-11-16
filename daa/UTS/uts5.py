def insertion_sort(data):
    perbandingan = 0

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0:
            perbandingan += 1

            if data[j] > key:
                data[j + 1] = data[j]
                j -= 1
            else:
                break

        data[j + 1] = key

    return perbandingan


def naive_matching(teks, pattern):
    posisi = []
    perbandingan = 0

    n = len(teks)
    m = len(pattern)

    for i in range(n - m + 1):
        cocok = True

        for j in range(m):
            perbandingan += 1

            if teks[i + j] != pattern[j]:
                cocok = False
                break

        if cocok:
            posisi.append(i)

    return posisi, perbandingan


data = [29, 10, 14, 37, 13, 8, 21]

teks = "data mining memanfaatkan data untuk analisis"
pattern = "data"

print("=== INSERTION SORT ===")
print("Data sebelum:", data)

hasil = data.copy()
jumlah = insertion_sort(hasil)

print("Data sesudah:", hasil)
print("Jumlah perbandingan:", jumlah)

print("\n=== STRING MATCHING ===")

posisi, jumlah_karakter = naive_matching(
    teks, pattern
)

print("Posisi pattern:", posisi)
print("Jumlah perbandingan karakter:", jumlah_karakter)