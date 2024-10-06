class CekUsia: #nama class
    #methode constructor
    def __init__(self,tahun_sekarang,tahun_lahir):
        self.tahun_sekarang = tahun_sekarang
        self.tahun_lahir = tahun_lahir

    #memuat methode HitungUsia
    def HitungUsia(self):
        return (self.tahun_sekarang - self.tahun_lahir)

#bagian input
ts=int(input("Masukkan Tahun Sekarang :"))
tl=int(input("Masukkan Tahun Lahir :"))

#membuat object
suci = CekUsia(ts,tl)

#memanggil method MenghitungUsia
print("Usia saya sekarang adalah:",suci.HitungUsia())

