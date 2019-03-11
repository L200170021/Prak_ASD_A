#============Nama = AdnanShafry Ari Purnama Aji===========#
#=====================NIM = L200170021 ===================#
#=====================Kelas = A ==========================#

class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai',len(self.teks),'karakter.')
    def perbarui(self,stringBaru):
        self.teks = stringBaru
    def apakahTerkandung(self, kata): ######NO.1A#######
        self.kata = kata
        if self.kata in self.teks:
            return True
        else:
            return False

    def hitungKonsonan(self): ###########NO.1B########
        a = self.teks
        vok = " AIUEOaiueo"	
        jml = 0	
        for b in a:
            if b.lower() not in vok :
                jml+=1
        return jml
    
    def hitungVokal(self): ###########NO.1C#########
        a = self.teks
        vok = " AIUEOaiueo"	
        jml = 0	
        for b in a:
            if b.lower() in vok :
                jml+=1
        return jml
    
###### Kode Untuk Eksekusi #######
## p9 = Pesan('Indonesia adalah negeri yang indah')
## p9.apakahTerkandung('ege')
## p9.apakahTerkandung('eka')
## p10 = Pesan('Surakarta')
## p10.hitungKonsonan()
## p10.hitungVokal()

#################################NO.2##################################
class Manusia(object):
    keadaan="lapar"
    def __init__(self,nama):
        self.nama=nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self,s):
        print("Saya baru saja makan", s)
        self.keadaan="kenyang"
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan="lapar"
    def mengalikanDenganDua(self,n):
        return n*2

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisialisasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangsaku = us
    def __str__(self):
        s = self.nama+", NIM"+str(self.NIM)\
            +". Tinggal di" +self.kotaTinggal \
            +". Uang saku Rp."+str(self.uangsaku)\
            +" tiap bulannya."
        return s
    def ambilNama(self):
        print (self.nama)
    def ambilNIM(self):
        print (self.NIM)
    def ambilUangSaku(self):
        print (self.uangsaku)
    def makan(self,s):
        """Metode ini menutupi makan -nya class Manusia. Mahasiswa kalau makan sambil belajar"""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan="Kenyang"
        
    def ambilKotaTinggal(self): #########NO.2A############
        print (self.kotaTinggal)
        
    def perbaruiKotaTinggal(self, baru): #############NO.2B##########
        self.kotaTinggal = baru
        
    def tambahUangSaku(self, uang):  ##########NO.2C##########
        self.uangsaku = self.uangsaku + uang
        
#################################NO.3##################################
##a = input("Masukkan Nama Anda : ")
##b = input("Masukkan NIM Anda : ")
##c = input("Masukkan Kota Tinggal Anda : ")
##d = input("Masukkan Uang Saku Anda : ")
    

########Kode Eksekusi#########
## m9 = Mahasiswa(a,b,c,d)
## m9.ambilNama()
## m9.ambilNIM()
## m9.ambilKotaTinggal()
## m9.ambilUangSaku()




        
#################################NO.4##################################
    listKuliah = []
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)



#################################NO.5##################################
    def hapusKuliah(self, item):
        self.listKuliah.remove(item)



#################################NO.6##################################
class SiswaSMA(Manusia):
    """Class SiswaSMA yang dibangun dari class Manusia"""
    def __init__(self,nama,no_induk,kelas,alamat):
        """Metode inisialisasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.no = no_induk
        self.kelas = kelas
        self.alamat = alamat
    def __str__(self):
        a = "Nama : "+self.nama+'\n'+"No Induk : "+str(self.no)+'\n'+"Tinggal di : "+self.alamat+'\n'+"Kelas : "+str(self.kelas)
        print (a)
    def ambilNama(self):
        print (self.nama)
    def ambilNoInduk(self):
        print (self.no)
    def ambilKelas(self):
        print (self.kelas)
    def ambilAlamat(self):
        print (self.alamat)





#################################NO.7##################################
class MhsTIF(Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanpeta(self):
        print('Python adalah core of the core,ahlinya ahli .')

##Dari class Manusia:
##    1. nama
##    2. keadaan
##    3. ucapkanSalam
##    4. makan
##    5. olahraga
##    6. mengalikanDenganDua
##
##Dari class Mahasiswa:
##    1. NIM
##    2. kotaTinggal
##    3. uangsaku
##    4. ambilNama
##    5. ambilNIM
##    6. ambilUangSaku
##    7. makan
##    8. ambilKotaTinggal
##    9. perbaruiKotaTinggal
##    10. tambahUangSaku
##    11. listKuliah
##    12. ambilKuliah
##    13. hapusKuliah
##
##Dari class MhsTIF:
##    1. katakanpeta
    
#############################Kode Eksekusi#############################     
m7 = Mahasiswa("Adnan","L200170021","Klaten",90000)
s1 = SiswaSMA("Adnan",17021,5,"Klaten")

## m9.ambilKotaTinggal()
## m9.perbaruiKotaTinggal('Surakarta')
## m9.ambilKotaTinggal()
## m9.ambilUangSaku()
## m9.tambahUangSaku(95000)
## m9.ambilUangSaku()





    
