class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        baru = Node(data)

        if self.head is None:
            self.head = baru
        else:
            akhir = self.head

            while akhir.next:
                akhir = akhir.next

            akhir.next = baru
            baru.prev = akhir

    def tampil(self):
        current = self.head

        while current:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")


dll = DoubleLinkedList()

dll.insert("Hafidz")
dll.insert("Andi")
dll.insert("Budi")

dll.tampil()