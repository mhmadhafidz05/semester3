n = int(input("Masukkan jumlah data : "))

data = []
jumlah = 0
operasi = 0

# Input data
for i in range(n):
    nilai = int(input(f"Masukkan nilai ke-{i + 1} : "))
    data.append(nilai)

# Menghitung jumlah
for i in range(n):
    jumlah = jumlah + data[i]
    operasi = operasi + 1

rata_rata = jumlah / n

print("\nData =", data)
print("Jumlah =", jumlah)
print("Rata-rata =", rata_rata)

print("\nJumlah operasi dasar =", operasi)

print("T(n) = n")
print(f"T({n}) = {n}")
print(f"Hasil T(n) = {operasi} operasi")

print("Kompleksitas waktu = O(n)")

print("\nBest Case    : O(n)")
print("Average Case : O(n)")
print("Worst Case   : O(n)")