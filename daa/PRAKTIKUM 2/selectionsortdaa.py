n = int(input("Masukkan jumlah data: "))

data = []

for i in range(n):
    nilai = int(input(f"Masukkan data ke-{i + 1}: "))
    data.append(nilai)

print("\nData sebelum diurutkan =", data)

perbandingan = 0
pertukaran = 0

# Selection Sort
for i in range(n - 1, 0, -1):
    imaks = 0

    for j in range(1, i + 1):
        perbandingan += 1

        if data[j] > data[imaks]:
            imaks = j

    # Pertukaran
    temp = data[i]
    data[i] = data[imaks]
    data[imaks] = temp

    pertukaran += 1

print("\nData setelah diurutkan =", data)

# Perhitungan kompleksitas
T_perbandingan = n * (n - 1) // 2
T_pertukaran = n - 1

print("\nJumlah Operasi:")
print("Perbandingan aktual =", perbandingan)
print("Pertukaran aktual   =", pertukaran)

print("\nRumus Kompleksitas Perbandingan:")
print("T(n) = n(n - 1) / 2")
print(f"T({n}) = {n}({n} - 1) / 2")
print(f"T({n}) = {T_perbandingan}")

print("\nKasus Kompleksitas Perbandingan:")
print(f"Tmin({n}) = {T_perbandingan}")
print(f"Tavg({n}) = {T_perbandingan}")
print(f"Tmax({n}) = {T_perbandingan}")

print("\nRumus Kompleksitas Pertukaran:")
print("T(n) = n - 1")
print(f"T({n}) = {n} - 1")
print(f"T({n}) = {T_pertukaran}")

print("\nBig-O:")
print("Best Case    = O(n^2)")
print("Average Case = O(n^2)")
print("Worst Case   = O(n^2)")