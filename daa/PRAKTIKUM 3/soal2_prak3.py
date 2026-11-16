
# def samaMatriks(A, B, n):
#     jumlah_perbandingan = 0

#     for i in range(n):
#         for j in range(n):
#             jumlah_perbandingan += 1

#             if A[i][j] != B[i][j]:
#                 return False, jumlah_perbandingan

#     return True, jumlah_perbandingan


# n = int(input("Masukkan ukuran matriks n: "))

# print("Masukkan Matriks A:")
# A = []
# for i in range(n):
#     baris = list(map(int, input(f"Baris {i+1}: ").split()))
#     A.append(baris)

# print("Masukkan Matriks B:")
# B = []
# for i in range(n):
#     baris = list(map(int, input(f"Baris {i+1}: ").split()))
#     B.append(baris)

# hasil, perbandingan = samaMatriks(A, B, n)

# print("\nHasil:", hasil)
# print("Jumlah perbandingan T(n):", perbandingan)

# if hasil:
#     print("Kedua matriks sama")
# else:
#     print("Kedua matriks berbeda")

# print("Best Case: O(1)")
# print("Worst Case: O(n^2)")






def samaMatriks(A, B, n):
    jumlah = 0

    for i in range(n):
        for j in range(n):
            jumlah += 1

            if A[i][j] != B[i][j]:
                return False, jumlah

    return True, jumlah


n = int(input("Masukkan ukuran matriks n: "))

A = []
B = []

print("\nMasukkan Matriks A:")
for i in range(n):
    baris = list(map(int, input(f"Baris {i+1}: ").split()))
    A.append(baris)

print("\nMasukkan Matriks B:")
for i in range(n):
    baris = list(map(int, input(f"Baris {i+1}: ").split()))
    B.append(baris)

hasil, jumlah = samaMatriks(A, B, n)

Tmin = 1
Tavg = (n**2 + 1) / 2
Tmax = n**2

print("\n=== ANALISIS T(n) ===")
print("Tmin(n) = 1")
print("Tavg(n) = (n^2 + 1) / 2")
print("Tmax(n) = n^2")

print(f"Tmin({n}) = {Tmin}")
print(f"Tavg({n}) = ({n}^2 + 1) / 2 = {Tavg}")
print(f"Tmax({n}) = {n}^2 = {Tmax}")

print("\n=== NOTASI ASIMTOTIK ===")
print("O-besar     = O(n^2)")
print("Omega-besar = Ω(1)")
print("Theta best  = Θ(1)")
print("Theta avg   = Θ(n^2)")
print("Theta worst = Θ(n^2)")

print("\n=== HASIL AKHIR ===")
print("Kedua matriks sama:", hasil)
print("Jumlah perbandingan aktual:", jumlah)
