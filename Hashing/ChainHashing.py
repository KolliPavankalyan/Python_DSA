from SinglyLinkedList import singlyLinkedList

class HashChain:
    def __init__(self):
        self.hashtable_size = 10
        self.hashtable = [0] * self.hashtable_size
        for i in range(self.hashtable_size):
            self.hashtable[i]=singlyLinkedList()

    def hashcode(self,key):
        return key % self.hashtable_size

    def insert(self,element):
        i = self.hashcode(element)
        self.hashtable[i].insertsorted(element)

    def search(self,key):
        i = self.hashcode(key)
        return self.hashtable[i].search(key) != -1

    def display(self):
        for i in range(self.hashtable_size):
            print('[',i,']', end= ' ')
            self.hashtable[i].display()
        print()

H = HashChain()
H.insert(54)
H.insert(78)
H.insert(64)
H.insert(92)
H.display()