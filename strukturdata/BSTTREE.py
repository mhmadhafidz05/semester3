# class Node:
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.height = 1

# class BST:
#     def insert(self, value):
#         self.root = self._insert(self.root, value)

#     def _insert(self, node, value):
#         if node is None:
#             return Node(value)

#         if value < node.value:
#             node.left = self._insert(node.left, value)

#         elif value > node.value:
#             node.right = self._insert(node.right, value)

#         else:
#             return node

#         self.update_height(node)
#         return self.rebalance(node)
#     def min_node(self, node):
#         if node.left is None:
#             return node

#         return self.min_node(node.left)

#     # DELETE REKURSIF
#     def delete(self, value):
#         self.root = self._delete(self.root, value)

#     def _delete(self, node, value):
#         if node is None:
#             return None

#         if value < node.value:
#             node.left = self._delete(node.left, value)

#         elif value > node.value:
#             node.right = self._delete(node.right, value)

#         else:
#             # Node tidak memiliki anak kiri
#             if node.left is None:
#                 return node.right

#             # Node tidak memiliki anak kanan
#             if node.right is None:
#                 return node.left

#             # Node memiliki dua anak
#             temp = self.min_node(node.right)
#             node.value = temp.value
#             node.right = self._delete(node.right, temp.value)

#         self.update_height(node)
#         return self.rebalance(node)

#     # SEARCH REKURSIF
#     def search(self, value):
#         return self._search(self.root, value)

#     def _search(self, node, value):
#         if node is None:
#             return False

#         if value == node.value:
#             return True

#         if value < node.value:
#             return self._search(node.left, value)

#         return self._search(node.right, value)

#     # INORDER REKURSIF
#     def inorder(self, node):
#         if node:
#             self.inorder(node.left)
#             print(node.value, end=" ")
#             self.inorder(node.right)

#     # PREORDER REKURSIF
#     def preorder(self, node):
#         if node:
#             print(node.value, end=" ")
#             self.preorder(node.left)
#             self.preorder(node.right)

#     # POSTORDER REKURSIF
#     def postorder(self, node):
#         if node:
#             self.postorder(node.left)
#             self.postorder(node.right)
#             print(node.value, end=" ")

#     # MENAMPILKAN POHON REKURSIF
#     def display(self, node, level=0, label="Root: "):
#         if node:
#             self.display(node.right, level + 1, "R--- ")

#             print(
#                 "    " * level
#                 + label
#                 + str(node.value)
#                 + f" (BF={self.balance_factor(node)})"
#             )

#             self.display(node.left, level + 1, "L--- ")
        
# tree = BST()

# while True:
#     print("\n===== AVLTree =====")
#     print("1. Insert")
#     print("2. Delete")
#     print("3. Search")
#     print("4. Inorder Traversal")
#     print("5. Preorder Traversal")
#     print("6. Postorder Traversal")
#     print("7. Tampilkan Pohon")
#     print("8. Keluar")

#     pilihan = input("Pilih menu (1-8): ")

#     if pilihan == "1":
#         try:
#             data = list(map(int, input(
#                 "Masukkan nilai (pisahkan spasi): "
#             ).split()))

#             if not data:
#                 print("Tidak ada nilai yang dimasukkan.")
#                 continue

#             for nilai in data:
#                 tree.insert(nilai)

#             print("\nData berhasil diproses!")
#             tree.display(tree.root)

#         except ValueError:
#             print("Masukkan angka yang valid!")

#     elif pilihan == "2":
#         try:
#             nilai = int(input("Masukkan nilai yang dihapus: "))

#             if tree.search(nilai):
#                 tree.delete(nilai)
#                 print("Data berhasil dihapus!")
#                 tree.display(tree.root)
#             else:
#                 print("Data tidak ditemukan.")

#         except ValueError:
#             print("Masukkan angka yang valid!")

#     elif pilihan == "3":
#         try:
#             nilai = int(input("Masukkan nilai yang dicari: "))

#             if tree.search(nilai):
#                 print("Data ditemukan!")
#             else:
#                 print("Data tidak ditemukan.")

#         except ValueError:
#             print("Masukkan angka yang valid!")

#     elif pilihan == "4":
#         print("Inorder:", end=" ")
#         tree.inorder(tree.root)
#         print()

#     elif pilihan == "5":
#         print("Preorder:", end=" ")
#         tree.preorder(tree.root)
#         print()

#     elif pilihan == "6":
#         print("Postorder:", end=" ")
#         tree.postorder(tree.root)
#         print()

#     elif pilihan == "7":
#         print("\nStruktur AVL Tree:")
#         if tree.root:
#             tree.display(tree.root)
#         else:
#             print("Pohon masih kosong.")

#     elif pilihan == "8":
#         print("Program selesai.")
#         break

#     else:
#         print("Pilihan tidak valid!")


# ======================================
# BINARY SEARCH TREE (BST) REKURSIF
# ======================================

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # INSERT REKURSIF
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        return node

    # SEARCH REKURSIF
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False

        if value == node.value:
            return True

        if value < node.value:
            return self._search(node.left, value)

        return self._search(node.right, value)

    # MENCARI NILAI MINIMUM REKURSIF
    def min_node(self, node):
        if node.left is None:
            return node

        return self.min_node(node.left)

    # DELETE REKURSIF
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)

        elif value > node.value:
            node.right = self._delete(node.right, value)

        else:
            # Jika tidak memiliki anak kiri
            if node.left is None:
                return node.right

            # Jika tidak memiliki anak kanan
            if node.right is None:
                return node.left

            # Jika memiliki dua anak
            temp = self.min_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        return node

    # INORDER REKURSIF
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    # PREORDER REKURSIF
    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # POSTORDER REKURSIF
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

    # MENAMPILKAN STRUKTUR POHON REKURSIF
    def display(self, node, level=0, label="Root: "):
        if node:
            self.display(node.right, level + 1, "R--- ")

            print("    " * level + label + str(node.value))

            self.display(node.left, level + 1, "L--- ")


# ======================================
# PROGRAM UTAMA
# ======================================

tree = BST()

while True:
    print("\n===== BINARY SEARCH TREE =====")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Tampilkan Pohon")
    print("8. Keluar")

    pilihan = input("Pilih menu (1-8): ")

    if pilihan == "1":
        try:
            data = list(map(int, input(
                "Masukkan nilai (pisahkan spasi): "
            ).split()))

            if not data:
                print("Tidak ada nilai yang dimasukkan.")
                continue

            for nilai in data:
                tree.insert(nilai)

            print("\nData berhasil dimasukkan!")
            tree.display(tree.root)

        except ValueError:
            print("Masukkan angka yang valid!")

    elif pilihan == "2":
        try:
            nilai = int(input("Masukkan nilai yang dihapus: "))

            if tree.search(nilai):
                tree.delete(nilai)
                print("Data berhasil dihapus!")
                tree.display(tree.root)
            else:
                print("Data tidak ditemukan!")

        except ValueError:
            print("Masukkan angka yang valid!")

    elif pilihan == "3":
        try:
            nilai = int(input("Masukkan nilai yang dicari: "))

            if tree.search(nilai):
                print("Data ditemukan!")
            else:
                print("Data tidak ditemukan!")

        except ValueError:
            print("Masukkan angka yang valid!")

    elif pilihan == "4":
        print("Inorder:", end=" ")
        tree.inorder(tree.root)
        print()

    elif pilihan == "5":
        print("Preorder:", end=" ")
        tree.preorder(tree.root)
        print()

    elif pilihan == "6":
        print("Postorder:", end=" ")
        tree.postorder(tree.root)
        print()

    elif pilihan == "7":
        print("\nStruktur BST:")
        if tree.root:
            tree.display(tree.root)
        else:
            print("Pohon masih kosong.")

    elif pilihan == "8":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
