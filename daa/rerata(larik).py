n = int(input("Masukkkan jumlah data :"))

data = []
jumlah = 0
operasi = 0

for i in range(n):
    nilai = int(input(f"Masukkan nilai ke-{i + 1} :"))
    data.append(nilai)
    jumlah = jumlah + nilai

for i in range(n):
    jumlah = jumlah + data[i]
    operasi = operasi + 1

rata_rata = jumlah / n

print("Data =", data)
print("Jumlah =", jumlah)
print("Rata-rata =", rata_rata)

print("Jumlah operasi dasar =", operasi)
print("T(n) =", n)
print("Kompleksitas waktu = O(n)")

print("\nAnalisis Kompleksitas Waktu:")
print("Jumlah operasi dasar =", operasi)
print("T(n) =", n)

print("Best Case    : O(n)")
print("Average Case : O(n)")
print("Worst Case   : O(n)")