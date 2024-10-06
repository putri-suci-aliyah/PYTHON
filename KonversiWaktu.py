class KonversiWaktu: #nama class
    # methode constructor
    def __init__(self,parameter_jumlah_detik):
        self.jumlah_detik = parameter_jumlah_detik

    #Memuat methode Hitung Detik
    def konversi_ke_detik(self):
        return self.jumlah_detik
    #Memuat methode Hitung Menit
    def konversi_ke_menit(self):
        return self.jumlah_detik / 60
    #Memuat methode Hitung jam
    def konversi_ke_jam(self):
        return self.jumlah_detik / 3600

#bagian input
input_detik = int(input("Masukan jumlah detik : "))

#membuat object
konveter = KonversiWaktu(input_detik)

#memanggil method Menghitung
print("Konversi ke detik : ", konveter.konversi_ke_detik(), " detik")
print("Konversi ke menit : ", konveter.konversi_ke_menit(), " menit")
print("Konversi ke jam  : ",  konveter.konversi_ke_jam(), " jam")