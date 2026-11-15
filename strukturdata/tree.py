class Node:
    def __init__(self, nama):
        self.nama = nama
        self.anak = []

    def tambah_anak(self, node):
        self.anak.append(node)


# Membuat Tree keluarga
ayah = Node("Ayah")

anak1 = Node("Andi")
anak2 = Node("Budi")
anak3 = Node("Citra")

ayah.tambah_anak(anak1)
ayah.tambah_anak(anak2)
ayah.tambah_anak(anak3)

anak1.tambah_anak(Node("Dina"))
anak1.tambah_anak(Node("Doni"))

anak2.tambah_anak(Node("Eka"))
anak3.tambah_anak(Node("Fani"))


# Fungsi menampilkan Tree
def tampilkan(node, level=0):
    print("   " * level + "|-- " + node.nama)

    for anak in node.anak:
        tampilkan(anak, level + 1)


print("STRUKTUR TREE KELUARGA")
tampilkan(ayah)