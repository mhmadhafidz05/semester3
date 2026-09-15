class StackBuku:
    def __init__(self):
        self.buku = []

    def insert(self, judul):
        self.buku.append(judul)
        print(f"{judul} telah ditambahkan")

    def delete(self):
        if len(self.buku) == 0:
            print("stack buku kosong")
        else:
            judul = self.buku.pop()
            print(f"{judul} buku telah dihabpus")

    def searching(self, judul):
        if judul in self.buku:
            print(f"{judul} berhasil ditemukan")
        else:
            print(f"{judul} tidak ditemukan")

    def display(self):
        print("ISI STACK BUKU")

        for judul in reversed(self.buku):
            print(judul)

stack = StackBuku()

stack.insert("Matematika")
stack.insert("Pemrograman")
stack.insert("Akidah")

print("================")

stack.delete()


print("================")

stack.searching("Pemrograman")


print("================")
 
stack.display()
