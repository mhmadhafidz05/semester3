def linear_search(data, target):
    perbandingan = 0

    for i in range(len(data)):
        perbandingan += 1

        if data[i] == target:
            return i, perbandingan

    return -1, perbandingan


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
        print("Iterasi", i, ":", data)

    return data


data = [25, 10, 30, 5, 20, 15, 35]

print("=== LINEAR SEARCH ===")
posisi, jumlah = linear_search(data, 20)

print("Nilai 20 ditemukan pada indeks:", posisi)
print("Jumlah perbandingan:", jumlah)

print("\n=== INSERTION SORT ===")
print("Data sebelum:", data)

hasil = insertion_sort(data.copy())

print("Data sesudah:", hasil)