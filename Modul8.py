#============Nama = Adnan Shafry Ari Purnama Aji===========#
#=====================NIM = L200170021 ===================#
#=====================Kelas = A ==========================#
#======================MODUL 8============================#

#nomer 1
class stack():
    def __init__(self):
        self.list = []
    def empty(self):
        return len(self.list) == 0
    def __len__(self):
        return len(self.list)
    def push(self, data):
        self.list.append(data)
    def pop(self):
        assert not self.empty(), 'No file'
        return self.list.pop()

def cetakHexa(angka):
    x = stack()

    if angka == 0:
        x.push(0)
    while angka != 0:
        sisa = angka % 16
        angka = angka // 16
        x.push(sisa)
    a = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    hasil = ''
    for i in range(len(x)):
        hsl += str(a[x.pop()])
    return hsl

#nomer 2
a = stack()         #Membuat objek dari kelas stack
for i in range(16): #Untuk i di dalam range (16)
    if i % 3 == 0:  #Jika i habis di bagi 3
        a.push(i)   #Meletakkan i di property a
        

#nomer 3
nilai = stack()         #Membuat objek dari kelas stack
for i in range(16):     #untuk i di dalam range 16
    if i % 3 == 0:      #jika i habis dibagi 3
        nilai.push(i)   #Meletakkan nilai i pada property nilai
    elif i % 4 == 0:    #tetapi jika i habis dibagi 4
        nilai.pop()     #Mengembalikan nilai dari item paling atas dari property nilai
                        #paling atas lalu menghapusnya
        
#nomer 4
class Queue():
    def __init__(self):
        self.qlist = []
    def is_empty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist.pop(0)
    def get_front_most(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[0]
    def get_rear_most(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[-1]

Y = Queue()
Y.enqueue(30)
Y.enqueue(26)
Y.enqueue(7)
Y.enqueue(18)
Y.enqueue(14)

print(Y.get_front_most())
print(Y.get_rear_most())
print(Y.qlist)

#nomer 5
class PriorityQueue():
    def __init__(self):
        self.qlist = []
    def __len__(self):
        return len(self.qlist)
    def is_empty(self):
        return len(self) == 0
    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)
    def dequeue(self):
        A = []
        for i in self.qlist:
            A.append(i)
        s = 0
        for i in range(1, len(self.qlist)):
            if A[i].priority < A[s].priority:
                s = i
        hasil = self.qlist.pop(s)
        return hasil.item

class _PriorityQEntry():
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

f = PriorityQueue()
f.enqueue("Topi",3)
f.enqueue("Baju",5)
f.enqueue("Celana",1)
f.enqueue("Jas",2)
f.enqueue("Jaket",4)

print(f.dequeue())
print(f.dequeue())
print(f.dequeue())
print(f.dequeue())
print(f.dequeue())
