class BilanganGanjil:
    def cek_ganjil(self):
        self.bilangan = float(input("Masukkan bilangan: "))

        if self.bilangan % 2 != 0:
            print(f"{self.bilangan} adalah bilangan ganjil.")
        else:
            print(f"{self.bilangan} bukan bilangan ganjil.")

obj = BilanganGanjil()
obj.cek_ganjil()