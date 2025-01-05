class Pembelian: #name class
    #membuat atribut
    total_pembelian = 0
    diskon = 0
    total_bayar = 0
    #membuat method
    def cekDiskon(self):
        print('Program Menghitung Diskon')
        self.total_pembelian = int(input('Masukkan total pembelian: '))
        self.diskon = self.total_pembelian*0.1

        if self.total_pembelian >= 1000000:
           self.diskon = self.total_pembelian*0.1
        else:
           self.diskon = 0
        print("Anda mendapatkan diskon sebesar:", self.diskon)



#membuat object
obj = Pembelian()

#memanggil method melalui object
obj.cekDiskon()

