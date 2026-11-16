#mencari elemen terbesar dalam larik


def cari_terbesar(data):
    terbesar = data[6]

    for i in range(1, len(data)):
        if data[i] > terbesar:
            terbesar = data[i]

    return terbesar

n = int(input("Masukkan jumlah data : "))

data = []

for i in range(n):
    nilai = int(input(f"Masukkan data ke-{i + 1}: "))
    data.append(nilai)

hasil = cari_terbesar(data)

print("Elemen terbesar adalah : ", hasil)

# data = [68, 77, 59, 87, 2, 99, 43]

# hasil = cari_terbesar(data)

# print("Elemen terbesar =", hasil)