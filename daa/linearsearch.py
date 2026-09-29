def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


data = [10, 20, 30, 40, 50]
target = int(input("Masukkan data yang dicari: "))

hasil = linear_search(data, target)

if hasil == -1:
    print("Data tidak ditemukan")
else:
    print("Data ditemukan pada indeks", hasil)