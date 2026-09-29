# # def pangkat (x, y):
# #     hasil = 1
# #     for i in range(y):
# #         hasil = x * hasil
# #     return hasil

# # x = input(int("Masukkan angka : "))
# # y = input(int("Masukkan angka : "))

# # print("hasil = ", pangkat (x,y))

def pangkat(x, y):
    hasil = 1
    for i in range(y):
        hasil = x * hasil
    return hasil


x = int(input("Masukkan angka: "))
y = int(input("Masukkan pangkat: "))

print("Hasil =", pangkat(x, y))





