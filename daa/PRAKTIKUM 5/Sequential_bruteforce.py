
def sequential_search(arr, target):
    perbandingan = 0

    for i in range(len(arr)):
        perbandingan += 1

        if arr[i] == target:
            return i, perbandingan

    return -1, perbandingan


# Input jumlah data
n = int(input("Masukkan jumlah data (n): "))

# Input elemen array
A = []
for i in range(n):
    nilai = int(input(f"Masukkan data ke-{i + 1}: "))
    A.append(nilai)

# Input angka yang dicari
target = int(input("Masukkan angka yang dicari: "))

print("\nArray:", A)

# Proses pencarian
posisi, perbandingan = sequential_search(A, target)

if posisi != -1:
    print(f"Data {target} ditemukan pada posisi ke-{posisi + 1}")
else:
    print(f"Data {target} tidak ditemukan")

print("\n=== Analisis Kompleksitas ===")
print("Jumlah data (n):", n)
print("Jumlah perbandingan:", perbandingan)
print("Best Case: Omega(1)")
print("Average Case: Theta(n)")
print("Worst Case: O(n)")
print("Space Complexity: O(1)")
