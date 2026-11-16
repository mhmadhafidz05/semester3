# def binary_search(lst, search):
#     lower_bound = 0
#     upper_bound =  len.lst - 1 
#     while True :
#         if upper_bound < upper_bound:
#             return -1
#         i = (lower_bound + upper_bound) // 2
#         if lst[i] < search:
#             lower_bound = i + 1
#         elif lst[i] > search:
#             upper_bound = i - 1
#         else :
#             return i

# lst = [10, 20, 30, 40, 50, 60, 70]

# search = int(input("Masukkan angka yang dicari: "))

# hasil = binary_search(lst, search)


def binary_search(data, target):
    lower_bound = 0
    upper_bound = len(data) - 1

    while lower_bound <= upper_bound:
        i = (lower_bound + upper_bound) // 2

        if data[i] == target:
            return i
        elif data[i] < target:
            lower_bound = i + 1
        else:
            upper_bound = i - 1

    return -1


data = [10, 20, 30, 40, 50, 60, 70]

target = int(input("Masukkan angka yang dicari: "))

hasil = binary_search(data, target)

print("Data ditemukan pada indeks", hasil)
