# # # # # # import numpy as np

# # # # # # data = np.array([10, 20, 30, 40, 50])

# # # # # # print(data)
# # # # # # print(type(data))
# # # # # # print(data.dtype)
# # # # # # print(data.shape) 

# # # # # import numpy as np

# # # # # n = int(input("Masukkan jumlah data: "))

# # # # # data = []

# # # # # for i in range(n):
# # # # #     angka = int(input(f"Masukkan data ke-{i + 1}: "))
# # # # #     data.append(angka)

# # # # # data = np.array(data)

# # # # # print("Isi array:", data)
# # # # # print("Jumlah seluruh elemen:", np.sum(data))

# # # # import numpy as np

# # # # nilai = np.array([75, 80, 85, 80, 60, 95, 90])

# # # # print("Jumlah:", np.sum(nilai))
# # # # print("Rata-rata:", np.mean(nilai))
# # # # print("Maksimum:", np.max(nilai))
# # # # print("Minimum:", np.min(nilai))
# # # # print("Standar Deviasi:", np.std(nilai))
# # # # print("Median:", np.median(nilai))

# # # import numpy as np

# # # nilai = np.array([55, 70, 85, 45, 90, 60, 75])

# # # hasil = nilai[nilai >= 70]

# # # print("Nilai >= 70:", hasil)

# # import numpy as np

# # A = np.array([
# #     [1, 2, 3],
# #     [4, 5, 6],
# #     [7, 8, 9]
# # ])

# # print("Matrix:")
# # print(A)

# # print("Diagonal utama:")
# # print(np.diag(A))

# # print("Jumlah diagonal utama:")
# # print(np.sum(np.diag(A)))

# import numpy as np

# A = np.array([
#     [1, 2],
#     [3, 4]
# ])

# B = np.array([
#     [5, 6],
#     [7, 8]
# ])

# print("A + B:")
# print(A + B)

# print("A - B:")
# print(A - B)

# print("Perkalian elemen:")
# print(A * B)

# print("Perkalian matriks:")
# print(A @ B)

import numpy as np

A = np.array([
    [10, 20, 30],
    [4, 5, 6]
])

print("Matrix awal:")
print(A)

reshape_A = A.reshape(3, 2)

print("Hasil Reshape:")
print(reshape_A)

transpose_A = A.T

print("Hasil Transpose:")
print(transpose_A)