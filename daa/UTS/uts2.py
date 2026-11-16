def proses(n):
    i = 1
    iterasi = 0

    print("Nilai awal i =", i)

    while i < n:
        i = i * 2
        iterasi += 1
        print("Iterasi", iterasi, ": i =", i)

    print("Total iterasi =", iterasi)


print("=== n = 20 ===")
proses(20)

print("\n=== n = 100 ===")
proses(100)

print("\n=== n = 10000 ===")
proses(10000)