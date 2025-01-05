class Pembelian: #name class
    #membuat atribut
    total_pembelian = 0
    diskon = 0
    total_bayar = 0
    #membuat method
    def cekDiskon(self):
        print('Program menghitung diskon')
        self.total_pembelian = int(input('Total pembelian: '))

        if self.total_pembelian>=2000000:
           self.diskon=self.total_pembelian*0.1
        else :
           self.diskon=0
        print("Total pembelian:", self.total_pembelian)
        print("Anda mendapatkan diskon sebesar:", self.diskon)

        self.total_bayar = self.total_pembelian-self.diskon
        print("Total bayar:", self.total_bayar)




#membuat object
obj = Pembelian()

#memanggil method melalui object
obj.cekDiskon()