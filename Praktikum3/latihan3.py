class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False



dll = DoublyLinkedList()

data_input = input("Masukkan elemen ke dalam Doubly Linked List (pisahkan dengan koma): ")

if data_input.strip() == "":
    print("Doubly Linked List kosong. Tidak ada elemen yang bisa dicari.")
else:
    elements = data_input.split(",")
    for item in elements:
        dll.insert_at_end(int(item.strip()))

    cari = int(input("Masukkan elemen yang ingin dicari: "))

    if dll.search(cari):
        print(f"Elemen {cari} ditemukan dalam Doubly Linked List.")
    else:
        print(f"Elemen {cari} tidak ditemukan dalam Doubly Linked List.")
