class stack:
    def __init__(self):
        self.data = []

    def insert(self, item):
        self.data.append(item)
        print(f"{item} berhasil ditambahkan")

    def delete(self):
        if len(self.data) == 0:
            print("data tidak ditemukan")
        else:
            item = self.data.pop()
            print(f"{item} data telah dihapus")
    
    def searching(self, item):
        if item in self.data:
            print(f"{item} ditemukan didalam stack")
        else:
            print(f"{item} tidak ditemukan didalam stack")

    def display(self):
        print("isi stack", self.data)

stack = stack()

stack.insert("yangmuliahafis")  
stack.insert("ismailbinmail")
stack.insert("arifyutaka")

stack.display()

stack.searching("arifyutaka")

stack.delete()

stack.display()




method insert apa" aja selain code insert