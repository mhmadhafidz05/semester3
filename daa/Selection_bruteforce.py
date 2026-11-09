
# def selection_sort(arr):
#     n = len(arr)

#     for i in range(n - 1):
#         min_idx = i

#         for j in range(i + 1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j

#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

#         print(f"Iterasi ke-{i + 1}: {arr}")

#     return arr


# # Data awal
# A = [89, 45, 68, 90, 29, 34, 17]

# print("Array sebelum diurutkan:", A)
# print("\nProses Selection Sort:")

# selection_sort(A)

# print("\nArray setelah diurutkan:", A)



def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        print(f"Iterasi ke-{i + 1}: {arr}")

    return arr


# Input jumlah data
n = int(input("Masukkan jumlah data (n): "))

# Input nilai array
A = []
for i in range(n):
    nilai = int(input(f"Masukkan data ke-{i + 1}: "))
    A.append(nilai)

print("\nArray sebelum diurutkan:", A)
print("\nProses Selection Sort:")

selection_sort(A)

print("\nArray setelah diurutkan:", A)

# Analisis kompleksitas
perbandingan = n * (n - 1) // 2

print("\n=== Analisis Kompleksitas ===")
print("Jumlah data (n):", n)
print("Jumlah iterasi utama:", max(0, n - 1))
print("Jumlah perbandingan C(n):", perbandingan)
print("Time Complexity: Theta(n^2)")
print("Space Complexity: O(1)")
