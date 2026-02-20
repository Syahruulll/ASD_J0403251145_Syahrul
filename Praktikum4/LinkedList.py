#========================================================
#Nama   : Syahrul Hidayatullah
#NIM    : J0403251145
#kelas  : A2    
#========================================================

#========================================================
#Implementasi Dasar: Node pada Linked List
#========================================================

class Node:
  #konstruktor yang dijalankan secara otomatis ketika class node dipanggil/diinstansi
  def __init__(self,data):
    self.data = data #menyimpan nilai atau data pada list
    self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)
    
    
#1) membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")


#2) menghubungkan node : A -> B -> C -> none
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#4) Traversal: Menelusuri node dari head sampai ke none
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya

#========================================================
#Implementasi Dasar: Stack 
#========================================================
