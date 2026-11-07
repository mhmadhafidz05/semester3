try:
    jarak = float(input("Masukkan jarak (km): "))

    if jarak <= 0:
        print("Jarak tidak valid")
    elif jarak <= 5:
        biaya = 10000
        print("Biaya: Rp", biaya)
    else:
        biaya = 10000 + (jarak - 5) * 2000
        print("Biaya: Rp", biaya)

except ValueError:
    print("Input harus berupa angka")