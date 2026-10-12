class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Membuat node
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Menghubungkan node
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2

# Menampilkan dari depan
print("Dari depan:")
print(node1.data, node1.next.data, node1.next.next.data)

# Menampilkan dari belakang
print("Dari belakang:")
print(node3.data, node3.prev.data, node3.prev.prev.data)