class BilanganBulat:
    def cek_bulat(self):
        self.bilangan = float(input("Masukkan bilangan: "))
        if self.bilangan.is_integer():
            print(f"{int(self.bilangan)} adalah bilangan bulat.")
        else:
            print(f"{self.bilangan} bukan bilangan bulat.")

obj  = BilanganBulat()
obj.cek_bulat()

