n = int(input("Masukkan jumlah data: "))

data = []

for i in range(n):
    nilai = int(input(f"Masukkan data ke-{i + 1}: "))
    data.append(nilai)

data.sort()

x = int(input("Masukkan nilai yang dicari: "))

i = 0
j = n - 1
ketemu = False
operasi = 0

while not ketemu and i <= j:
    mid = (i + j) // 2
    operasi = operasi + 1

    if data[mid] == x:
        ketemu = True

    elif data[mid] < x:
        i = mid + 1

    else:
        j = mid - 1

if ketemu:
    idx = mid + 1
    print("\nNilai", x, "ditemukan pada posisi ke-", idx)
else:
    idx = 0
    print("\nNilai", x, "tidak ditemukan")

print("Jumlah perbandingan aktual =", operasi)

import math

print("\nKompleksitas Waktu:")
print("Tmin(n) = 1")
print("Tmax(n) =", math.floor(math.log2(n)) + 1)

print("\nBig-O:")
print("Best Case  = O(1)")
print("Worst Case = O(log n)")