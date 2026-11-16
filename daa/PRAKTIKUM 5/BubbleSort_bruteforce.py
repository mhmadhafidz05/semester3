
def bubble_sort(arr):
    n = len(arr)
    perbandingan = 0
    pertukaran = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            perbandingan += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                pertukaran += 1

        print(f"Iterasi ke-{i + 1}: {arr}")

    return perbandingan, pertukaran


# Input data
n = int(input("Masukkan jumlah data (n): "))

A = []
for i in range(n):
    nilai = int(input(f"Masukkan data ke-{i + 1}: "))
    A.append(nilai)

print("\nArray sebelum diurutkan:", A)
print("\nProses Bubble Sort:")

perbandingan, pertukaran = bubble_sort(A)

print("\nArray setelah diurutkan:", A)

print("\n=== Analisis Kompleksitas ===")
print("Jumlah data (n):", n)
print("Jumlah perbandingan:", perbandingan)
print("Jumlah pertukaran:", pertukaran)
print("Time Complexity: Theta(n^2)")
print("Space Complexity: O(1)")
