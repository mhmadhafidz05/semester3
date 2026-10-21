# # # n = int(input("Masukkan jumlah data: "))

# # # data = []

# # # for i in range(n):
# # #     nilai = int(input(f"Masukkan data ke-{i + 1}: "))
# # #     data.append(nilai)

# # # data.sort()

# # # x = int(input("Masukkan nilai yang dicari: "))

# # # i = 0
# # # j = n - 1
# # # ketemu = False
# # # operasi = 0

# # # while not ketemu and i <= j:
# # #     mid = (i + j) // 2
# # #     operasi = operasi + 1

# # #     if data[mid] == x:
# # #         ketemu = True

# # #     elif data[mid] < x:
# # #         i = mid + 1

# # #     else:
# # #         j = mid - 1

# # # if ketemu:
# # #     idx = mid + 1
# # #     print("\nNilai", x, "ditemukan pada posisi ke-", idx)
# # # else:
# # #     idx = 0
# # #     print("\nNilai", x, "tidak ditemukan")

# # # print("Jumlah perbandingan aktual =", operasi)

# # # import math

# # # print("\nKompleksitas Waktu:")
# # # print("Tmin(n) = 1")
# # # print("Tmax(n) =", math.floor(math.log2(n)) + 1)

# # # print("\nBig-O:")
# # # print("Best Case  = O(1)")
# # # print("Worst Case = O(log n)")

# # import math

# # n = int(input("Masukkan jumlah data: "))

# # data = []

# # for i in range(n):
# #     nilai = int(input(f"Masukkan data ke-{i + 1}: "))
# #     data.append(nilai)

# # data.sort()

# # x = int(input("Masukkan nilai yang dicari: "))

# # i = 0
# # j = n - 1
# # ketemu = False
# # operasi = 0

# # while not ketemu and i <= j:
# #     mid = (i + j) // 2
# #     operasi = operasi + 1

# #     if data[mid] == x:
# #         ketemu = True
# #     elif data[mid] < x:
# #         i = mid + 1
# #     else:
# #         j = mid - 1

# # if ketemu:
# #     idx = mid + 1
# #     print("\nNilai", x, "ditemukan pada posisi ke-", idx)
# # else:
# #     idx = 0
# #     print("\nNilai", x, "tidak ditemukan")

# # log_n = math.log2(n)
# # tmax = math.floor(log_n) + 1

# # print("\nData =", data)
# # print("Jumlah perbandingan aktual =", operasi)

# # print("\nKompleksitas Waktu:")
# # print("Tmin(n) = 1")
# # print("log2(n) =", log_n)
# # print("Tmax(n) =", tmax)

# # print("\nBig-O:")
# # print("Best Case  = O(1)")
# # print("Worst Case = O(log n)")


# import math

# n = int(input("Masukkan jumlah data: "))

# data = []

# for i in range(n):
#     nilai = int(input(f"Masukkan data ke-{i + 1}: "))
#     data.append(nilai)

# data.sort()

# x = int(input("Masukkan nilai yang dicari: "))

# i = 0
# j = n - 1
# ketemu = False
# operasi = 0

# while not ketemu and i <= j:
#     mid = (i + j) // 2
#     operasi += 1

#     if data[mid] == x:
#         ketemu = True
#     elif data[mid] < x:
#         i = mid + 1
#     else:
#         j = mid - 1

# if ketemu:
#     print("\nNilai", x, "ditemukan pada posisi ke-", mid + 1)
# else:
#     print("\nNilai", x, "tidak ditemukan")

# # Hitung kompleksitas
# best_case = 1
# nilai_log = math.log2(n)
# worst_case = math.floor(nilai_log) + 1

# print("\nData =", data)
# print("Jumlah perbandingan aktual =", operasi)

# print("\nPerhitungan Kompleksitas Waktu:")

# print("Best Case:")
# print("Tmin(n) =", best_case)

# print("\nWorst Case:")
# print("log2(", n, ") =", round(nilai_log, 2))
# print("Tmax(n) =", worst_case)

import math

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

while i <= j and not ketemu:
    operasi = operasi + 1
    mid = (i + j) // 2

    if data[mid] == x:
        ketemu = True
    elif data[mid] < x:
        i = mid + 1
    else:
        j = mid - 1

if ketemu:
    print("\nNilai", x, "ditemukan pada posisi ke-", mid + 1)
else:
    print("\nNilai", x, "tidak ditemukan")

print("\nData terurut =", data)
print("Jumlah perbandingan aktual =", operasi)

print("\nRumus Kompleksitas Waktu:")
print("T(n) = T(n/2) + 1")
print("T(n) = log2(n)")

print(f"\nT({n}) = log2({n})")
print(f"T({n}) = {math.log2(n):.2f}")

print("\nKasus Kompleksitas:")
print("Tmin(n) = 1")
print(f"Tavg(n) = log2({n}) = {math.log2(n):.2f}")
print(f"Tmax(n) = log2({n}) = {math.log2(n):.2f}")

print("\nBig-O:")
print("Best Case    = O(1)")
print("Average Case = O(log n)")
print("Worst Case   = O(log n)")