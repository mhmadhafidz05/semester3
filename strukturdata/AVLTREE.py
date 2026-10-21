
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    # def __init__(self):
    #     self.root = None

    # # Mengambil tinggi node
    # def height(self, node):
    #     return node.height if node else 0

    # # Menghitung Balance Factor
    # def balance_factor(self, node):
    #     if not node:
    #         return 0

    #     return self.height(node.left) - self.height(node.right)

    # # Memperbarui tinggi node
    # def update_height(self, node):
    #     node.height = 1 + max(
    #         self.height(node.left),
    #         self.height(node.right)
    #     )

    # # Rotasi kanan (LL)
    # def right_rotate(self, z):
    #     y = z.left
    #     temp = y.right

    #     y.right = z
    #     z.left = temp

    #     self.update_height(z)
    #     self.update_height(y)

    #     return y

    # # Rotasi kiri (RR)
    # def left_rotate(self, z):
    #     y = z.right
    #     temp = y.left

    #     y.left = z
    #     z.right = temp

    #     self.update_height(z)
    #     self.update_height(y)

        return y

    # Menyeimbangkan AVL Tree
    # def rebalance(self, node):
    #     bf = self.balance_factor(node)

    #     # Left Heavy
    #     if bf > 1:
    #         if self.balance_factor(node.left) < 0:
    #             print("Rotasi LR (Left-Right)")
    #             node.left = self.left_rotate(node.left)
    #         else:
    #             print("Rotasi LL (Right Rotation)")

    #         return self.right_rotate(node)

    #     # Right Heavy
    #     if bf < -1:
    #         if self.balance_factor(node.right) > 0:
    #             print("Rotasi RL (Right-Left)")
    #             node.right = self.right_rotate(node.right)
    #         else:
    #             print("Rotasi RR (Left Rotation)")

    #         return self.left_rotate(node)

        return node

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

        else:
            return node

        self.update_height(node)
        return self.rebalance(node)

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
            # Node tidak memiliki anak kiri
            if node.left is None:
                return node.right

            # Node tidak memiliki anak kanan
            if node.right is None:
                return node.left

            # Node memiliki dua anak
            temp = self.min_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        self.update_height(node)
        return self.rebalance(node)

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

    # MENAMPILKAN POHON REKURSIF
    def display(self, node, level=0, label="Root: "):
        if node:
            self.display(node.right, level + 1, "R--- ")

            print(
                "    " * level
                + label
                + str(node.value)
                + f" (BF={self.balance_factor(node)})"
            )

            self.display(node.left, level + 1, "L--- ")


# ======================================
# PROGRAM UTAMA
# ======================================

tree = AVLTree()

while True:
    print("\n===== AVLTree =====")
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

            print("\nData berhasil diproses!")
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
                print("Data tidak ditemukan.")

        except ValueError:
            print("Masukkan angka yang valid!")

    elif pilihan == "3":
        try:
            nilai = int(input("Masukkan nilai yang dicari: "))

            if tree.search(nilai):
                print("Data ditemukan!")
            else:
                print("Data tidak ditemukan.")

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
        print("\nStruktur AVL Tree:")
        if tree.root:
            tree.display(tree.root)
        else:
            print("Pohon masih kosong.")

    elif pilihan == "8":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
