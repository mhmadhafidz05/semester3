class Stack:
    def __init__(self):
        self.data = []

    # Insert data ke stack
    def insert(self, item):
        self.data.append(item)
        print(f"{item} berhasil ditambahkan.")

    # Delete data paling atas dari stack
    def delete(self):
        if len(self.data) == 0:
            print("Stack kosong, tidak ada data yang bisa dihapus.")
        else:
            item = self.data.pop()
            print(f"{item} berhasil dihapus.")

    # Searching data di dalam stack
    def searching(self, item):
        if item in self.data:
            print(f"{item} ditemukan di dalam stack.")
        else:
            print(f"{item} tidak ditemukan di dalam stack.")

    # Menampilkan isi stack
    def display(self):
        print("Isi Stack:", self.data)


# Membuat object Stack
stack = Stack()

# Insert data
stack.insert("Hafidz")
stack.insert("Andi")
stack.insert("Budi")

# Menampilkan stack
stack.display()

# Searching
stack.searching("Andi")

# Delete
stack.delete()

# Menampilkan stack setelah delete
stack.display() 