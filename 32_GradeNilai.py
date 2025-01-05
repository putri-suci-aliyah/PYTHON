class GradeNilai: #name class
    #membuat atribut
    NRP = ""
    Nama = ""
    Nil_Tugas = 0
    Nil_Quiz = 0
    Nil_UTS = 0
    Nil_UAS = 0
    Nil_akhir = 0
    keterangan = ""
    Grade = ""

    #membuat methode constrictor
    def __init__(self, NRP, Nama,Nil_Tugas, Nil_Quiz, Nil_UTS, Nil_UAS):
        self.NRP = NRP
        self.Nama = Nama
        self.Nil_Tugas = Nil_Tugas
        self.Nil_Quiz = Nil_Quiz
        self.Nil_UTS = Nil_UTS
        self.Nil_UAS = Nil_UAS

    #membuat method untuk menghitung nilai akhir
    def HitungNilaiakhir(self):
        self.Nil_akhir = self.Nil_Tugas*0.1 + self.Nil_Quiz*0.1 + self.Nil_UTS*0.3 + self.Nil_UAS*0.5

        #cek lulus atau tidak
        if self.Nil_akhir>=60:
            self.keterangan = "Lulus"
        else :
            self.keterangan = "Tidak Lulus"

        #cek grade nilai
        if self.Nil_akhir>=85:
            self.Grade = "A"
        elif self.Nil_akhir>=70:
            self.Grade = "B"
        elif self.Nil_akhir>=60:
            self.Grade = "C"
        elif self.Nil_akhir>=50:
            self.Grade = "D"
        else:
            self.Grade = "E"

        #menampilkan nilai akhir, keterangan dan grade nilai
        print("Nilai Akhir      \t\t:", self.Nil_akhir)
        print("Keterangan       \t\t:", self.keterangan)
        print("Grade Nilai      \t\t:", self.Grade)

#bagian input
NRP = str(input("Masukkan NRP\t\t\t: "))
Nama = str(input("Masukkan Nama\t\t\t: "))
Nil_Tugas=float(input("Masukkan Nilai Tugas\t: "))
Nil_Quiz=float(input("Masukkan Nilai Quiz  \t: "))
Nil_UTS=float(input("Masukkan Nilai UTS    \t: "))
Nil_UAS=float(input("Masukkan Nilai UAS    \t: "))

#membuat object
mhs = GradeNilai(NRP, Nama, Nil_Tugas, Nil_Quiz, Nil_UTS, Nil_UAS)

#memanggil output melalui methode
print()
print("Program Menghitung Nilai Akhir")
print("------------------------------")
mhs.HitungNilaiakhir()
print("------------------------------")