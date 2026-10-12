n = int(input("Masukkkan jumlah data :"))

data = []
jumlah = 0

for i in range(n):
    nilai = int(input(f"Masukkan nilai ke-{i + 1} :"))
    data.append(nilai)
    jumlah = jumlah + nilai

maks = data[0]
k = 1
operasi = 0

while k < n:
    operasi = operasi + 1
    if data[k] > maks:
        maks = data[k]

    k = k + 1

print("Data =", data)
print("Nilai Terbesar =", maks)

print("Jumlah Operasi =", operasi)
print("T(n) =", n - 1)
print("Kompleksitas waktu = O(n)")