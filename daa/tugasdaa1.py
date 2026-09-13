def find_maximum(A):
    n = len(A)

    if n == 0:
        return "Array kosong"

    max_value = A[0]
    i = 1

    while i < n:
        if A[i] > max_value:
            max_value = A[i]

        i = i + 1

    return max_value


A = [7, 3, 12, 5, 9]

hasil = find_maximum(A)

print("Nilai terbesar adalah:", hasil)