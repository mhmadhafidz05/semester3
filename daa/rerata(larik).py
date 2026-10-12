n = int(input("Masukkkan jumlah data :"))

data = []
jumlah = 0

for i in range(n):
    nilai = int(input(f"Masukkan nilai ke-{i + 1} :"))
    data.append(nilai)
    jumlah = jumlah + nilai

rata_rata = jumlah / n

print("Data =", data)
print("Jumlah =", jumlah)
print("Rata-rata =", rata_rata)
