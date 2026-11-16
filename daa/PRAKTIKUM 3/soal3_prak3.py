
n = int(input("Masukkan nilai n: "))

x = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, j + 1):
            x = x + 1

T = (n**2 * (n + 1)) // 2

print("\n=== ANALISIS T(n) ===")
print("T(n) = n x (1 + 2 + ... + n)")
print("T(n) = n x (n(n+1) / 2)")
print(f"T({n}) = {n} x ({n}({n}+1) / 2)")
print(f"T({n}) = {n} x {n*(n+1)//2}")
print(f"T({n}) = {T}")

print("\n=== MIN, AVG, MAX ===")
print(f"Tmin({n}) = {T}")
print(f"Tavg({n}) = {T}")
print(f"Tmax({n}) = {T}")

print("\n=== NOTASI ASIMTOTIK ===")
print("O-besar     = O(n^3)")
print("Omega-besar = Ω(n^3)")
print("Theta-besar = Θ(n^3)")

print("\n=== HASIL AKHIR ===")
print("Jumlah assignment:", x)
