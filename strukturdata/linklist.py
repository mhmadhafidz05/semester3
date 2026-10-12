class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node
            new_node.prev = current

        print(data, "berhasil ditambahkan")

    def delete(self, data):
        current = self.head

        while current is not None:
            if current.data == data:

                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev

                print(data, "berhasil dihapus")
                return

            current = current.next

        print(data, "tidak ditemukan")

    def searching(self, data):
        current = self.head
        posisi = 0

        while current is not None:
            if current.data == data:
                print(data, "ditemukan pada posisi", posisi)
                return

            current = current.next
            posisi += 1

        print(data, "tidak ditemukan")

    def display_forward(self):
        current = self.head

        print("Data dari depan:", end=" ")

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")

    def display_backward(self):
        current = self.head

        if current is None:
            print("Data kosong")
            return

        while current.next is not None:
            current = current.next

        print("Data dari belakang:", end=" ")

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev

        print("None")


dll = DoubleLinkedList()

dll.insert("Hafidz")
dll.insert("Andi")
dll.insert("Budi")
dll.insert("Rizky")

dll.display_forward()
dll.display_backward()

dll.searching("Andi")

dll.delete("Budi")

dll.display_forward()