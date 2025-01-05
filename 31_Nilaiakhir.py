class Nilaiakhir: #name class
    #membuat atribut
    nilai_tugas = 0
    nilai_quiz = 0
    nilai_UTS = 0
    nilai_UAS = 0
    nilai_akhir = 0
    keterangan = ""
    #membuat method
    def cetakNilaiakhir(self):
        print('Program menghitung Nilai Akhir')
        self.nilai_tugas = float(input('Masukkan nilai tugas: '))
        self.nilai_quiz = float(input('Masukkan nilai quiz: '))
        self.nilai_UTS = float(input('Masukkan nilai UTS: '))
        self.nilai_UAS = float(input('Masukkan nilai UAS: '))
        self.nilai_akhir = self.nilai_tugas*0.1 + self.nilai_quiz*0.1 + self.nilai_UTS*0.3 + self.nilai_UAS*0.5

        if self.nilai_akhir>=60:
            self.keterangan = "Lulus"
        else :
            self.keterangan = "Tidak Lulus"
        print("Nilai Akhir Anda:", self.nilai_akhir)
        print("Keterangan:", self.keterangan)





#membuat object
Suci = Nilaiakhir()

#memanggil method melalui object
Suci.cetakNilaiakhir()