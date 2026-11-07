
def fibonacci(n):
    global operasi, kedalaman, max_kedalaman

    operasi += 1
    kedalaman += 1
    max_kedalaman = max(max_kedalaman, kedalaman)

    if n <= 1:
        hasil = n
    else:
        hasil = fibonacci(n - 1) + fibonacci(n - 2)

    kedalaman -= 1
    return hasil


n = int(input("Masukkan jumlah bilangan Fibonacci: "))

if n <= 0:
    print("Masukkan nilai lebih dari 0!")
else:
    print("\n=== DERET FIBONACCI ===")

    for i in range(n):
        operasi = 0
        kedalaman = 0
        max_kedalaman = 0

        hasil = fibonacci(i)
        print(hasil, end=" ")

    # Analisis seluruh proses pencetakan deret
    operasi = 0
    kedalaman = 0
    max_kedalaman = 0

    for i in range(n):
        fibonacci(i)

    print("\n\n=== ANALISIS KOMPLEKSITAS ===")
    print("T(n) =", operasi, "pemanggilan fungsi")
    print("S(n) =", max_kedalaman, "level rekursi")

    print("\nKompleksitas Waktu:")
    print("Big-O  : O(2^n)")
    print("Omega  : Ω(φ^n)")
    print("Theta  : Θ(φ^n)")

    print("\nKompleksitas Ruang:")
    print("Big-O  : O(n)")
    print("Omega  : Ω(n)")
    print("Theta  : Θ(n)")
