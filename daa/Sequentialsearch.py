# n = int(input("Masukkan jumlah data: "))

# data = []

# for i in range(n):
#     nilai = int(input(f"Masukkan data ke-{i + 1}: "))
#     data.append(nilai)

# x = int(input("Masukkan nilai yang dicari: "))

# k = 0
# ketemu = False
# operasi = 0

# while k < n and not ketemu:
#     operasi = operasi + 1

#     if data[k] == x:
#         ketemu = True
#     else:
#         k = k + 1

# if ketemu:
#     idx = k + 1
#     print("\nNilai", x, "ditemukan pada posisi ke-", idx)
# else:
#     idx = 0
#     print("\nNilai", x, "tidak ditemukan")

# print("\nData =", data)
# print("Jumlah operasi pencarian =", operasi)

# print("\nKompleksitas Waktu:")
# print("Tmin(n) = 1")
# print("Tavg(n) = (n + 1) / 2")
# print("Tmax(n) = n")

# print("Best Case    = O(1)")
# print("Average Case = O(n)")
# print("Worst Case   = O(n)")

n = int(input("Masukkan jumlah data: "))

data = []

for i in range(n):
    nilai = int(input(f"Masukkan data ke-{i + 1}: "))
    data.append(nilai)

x = int(input("Masukkan nilai yang dicari: "))

k = 0
ketemu = False
operasi = 0

while k < n and not ketemu:
    operasi = operasi + 1

    if data[k] == x:
        ketemu = True
    else:
        k = k + 1

if ketemu:
    idx = k + 1
    print("\nNilai", x, "ditemukan pada posisi ke-", idx)
else:
    idx = 0
    print("\nNilai", x, "tidak ditemukan")

print("Jumlah perbandingan aktual =", operasi)

print("\nKompleksitas Waktu:")
print("Tmin(n) = 1")
print("Tavg(n) =", (n + 1) / 2)
print("Tmax(n) =", n)

print("\nBig-O:")
print("Best Case    = O(1)")
print("Average Case = O(n)")
print("Worst Case   = O(n)")