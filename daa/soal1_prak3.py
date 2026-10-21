
n = int(input("Masukkan nilai n: "))

a = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        for k in range(j, n + 1):
            a = a + 1

T = n * (n + 1) * (2 * n + 1) // 6

print("\n=== ANALISIS T(n) ===")
print("T(n) = n^2 + (n-1)^2 + ... + 1^2")
print("T(n) = n(n+1)(2n+1) / 6")
print(f"T({n}) = {n}({n}+1)(2({n})+1) / 6")
print(f"T({n}) = {T}")

print("\n=== MIN, AVG, MAX ===")
print("Tmin(n) =", T)
print("Tavg(n) =", T)
print("Tmax(n) =", T)

print("\n=== NOTASI ASIMTOTIK ===")
print("O-besar     = O(n^3)")
print("Omega-besar = Ω(n^3)")
print("Theta-besar = Θ(n^3)")

print("\nJumlah operasi aktual:", a)
