class GajiPegawai: #Nama class
    #Membuat atribut
    Nama = ""
    Golongan = ""
    Status_nikah = ""
    Jumlah_anak = 0

    Gaji_pokok = 0
    Tunjangan_jabatan = 0
    Tunjangan_istri = 0
    Tunjangan_anak = 0
    Total_gaji = 0

    # membuat methode constrictor
    def __init__(self,Nama, Status_nikah, Jumlah_anak):
        self.Nama = Nama
        self.Golongan = Golongan
        self.Status_nikah = Status_nikah
        self.Jumlah_anak = Jumlah_anak

    # membuat method untuk menghitung gaji
    def HitungGaji(self):
        #cek untuk menentukan Gaji Pokok
        if self.Golongan=="I":
            self.Gaji_pokok = 300000
        elif self.Golongan=="II":
            self.Gaji_pokok = 500000
        else: self.Gaji_pokok = 750000

        #cek untuk menentukan tunjangan jabatan
        self.Tunjangan_jabatan = 0.35 * self.Gaji_pokok

        # cek untuk menentukan tunjangan istri
        if self.Status_nikah=="Y":
            self.Tunjangan_istri = 0.30 * self.Gaji_pokok
            if self.Jumlah_anak>=3:
                self.Tunjangan_anak = 0.75 * self.Gaji_pokok
            else:
                self.Tunjangan_anak = 0.25 * self.Jumlah_anak * self.Gaji_pokok
        else:
            self.Tunjangan_istri = 0
            self.Tunjangan_anak = 0

        #hitung total gaji
        self.Total_gaji = self.Gaji_pokok + self.Tunjangan_jabatan + self.Tunjangan_istri + self.Tunjangan_anak

        #bagian output
        print()
        print("Gaji Pokok                   \t\t:",self.Gaji_pokok)
        print("Tunjangan Jabatan            \t\t:", self.Tunjangan_jabatan)
        print("Tunjangan Istri              \t\t:", self.Tunjangan_istri)
        print("Tunjangan Anak               \t\t:",self.Tunjangan_anak)
        print("Total Gaji                   \t\t:", self.Total_gaji)

#bagian input
Nama = str(input("Masukkan Nama Pegawai           \t: "))
Golongan = str(input("Masukkan Golongan (I/II/III)    \t: "))
Status_nikah = str(input("Masukkan Status Nikah (Y/T)     \t: "))
Jumlah_anak = int(input("Masukkan Jumlah Anak            \t: "))

#membuat object
pegawai = GajiPegawai(Nama, Status_nikah, Jumlah_anak)

#memanggil methode melalui object
pegawai.HitungGaji()





