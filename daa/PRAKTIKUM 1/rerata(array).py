#menghitung rata rata dalam larik 

def hitung_rerata(data):
    total = 0

    for i in range(len(data)):
        total = total + data[i]

    rerata = total / len(data)
    return rerata


n = int(input("Masukkan jumlah data: "))

data = []

for i in range(n):
    nilai = int(input(f"Masukkan data ke-{i + 1}: "))
    data.append(nilai)

hasil = hitung_rerata(data)

print("Rerata =", hasil)