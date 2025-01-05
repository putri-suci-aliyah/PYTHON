class Pembelian:

    total_pembelian = 0
    diskon = 0
    total_bayar = 0
    def cekDiskon(self):
        print("Program Menghitung Diskon")
        self.total_pembelian = int(input("Total Pembelian: "))

        if self.total_pembelian>=20000:
           self.diskon=self.total_pembelian*0.1
        else:
            self.diskon = 0
        print("Total Pembelian:", self.total_pembelian)
        print("Anda mendapatkan diskon sebesar:" , self.diskon)

        self.total_bayar = self.total_pembelian-self.diskon
        print("Total bayar:" , self.total_bayar)

obj = Pembelian()
obj.cekDiskon()



