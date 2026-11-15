
class Queue:
    def __init__(self):
        self.items = []

    # Menambahkan data ke antrian
    def enqueue(self, data):
        self.items.append(data)
        print(f"Data {data} berhasil ditambahkan.")

    # Menghapus data paling depan
    def dequeue(self):
        if self.is_empty():
            print("Queue kosong, tidak ada data yang dihapus.")
        else:
            data = self.items.pop(0)
            print(f"Data {data} berhasil dihapus.")

    # Melihat data paling depan
    def peek(self):
        if self.is_empty():
            print("Queue kosong.")
        else:
            print(f"Data paling depan: {self.items[0]}")

    # Memeriksa apakah queue kosong
    def is_empty(self):
        return len(self.items) == 0

    # Mencari data dalam queue
    def search(self, data):
        if data in self.items:
            posisi = self.items.index(data) + 1
            print(f"Data {data} ditemukan pada posisi {posisi}.")
        else:
            print(f"Data {data} tidak ditemukan.")

    # Menampilkan seluruh antrian
    def display(self):
        if self.is_empty():
            print("Queue masih kosong.")
        else:
            print("\nAntrian (Depan -> Belakang):")
            print(" -> ".join(map(str, self.items)))

    # Menghitung jumlah data
    def size(self):
        print(f"Jumlah data dalam queue: {len(self.items)}")


# Program utama
queue = Queue()

while True:
    print("\n===== MENU QUEUE =====")
    print("1. Enqueue (Tambah Data)")
    print("2. Dequeue (Hapus Data)")
    print("3. Peek (Lihat Data Depan)")
    print("4. Search (Cari Data)")
    print("5. Display (Tampilkan Queue)")
    print("6. Size (Jumlah Data)")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        data = input("Masukkan data: ")
        queue.enqueue(data)

    elif pilihan == "2":
        queue.dequeue()

    elif pilihan == "3":
        queue.peek()

    elif pilihan == "4":
        data = input("Masukkan data yang dicari: ")
        queue.search(data)

    elif pilihan == "5":
        queue.display()

    elif pilihan == "6":
        queue.size()

    elif pilihan == "7":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
