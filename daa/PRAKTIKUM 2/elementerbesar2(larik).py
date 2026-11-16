n = int(input("Masukkan jumlah data : "))

data = []

for i in range(n):
    nilai = int(input(f"Masukkan nilai ke-{i + 1} : "))
    data.append(nilai)

maks = data[0]
k = 1
operasi = 0

while k < n:
    operasi = operasi + 1

    if data[k] > maks:
        maks = data[k]

    k = k + 1

print("\nData =", data)
print("Nilai Terbesar =", maks)

print("\nJumlah Operasi =", operasi)
print("T(n) = n - 1")
print(f"T({n}) = {n} - 1")
print(f"T({n}) = {n - 1}")

print("Kompleksitas waktu = O(n)")

print("\nBest Case    : O(n)")
print("Average Case : O(n)")
print("Worst Case   : O(n)")