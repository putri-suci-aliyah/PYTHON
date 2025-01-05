class Pilihan:
    def cek_ganjil(self, bilangan):
        if bilangan % 2 != 0:
            print(f"{bilangan} adalah bilangan ganjil.")
        else:
            print(f"{bilangan} bukan bilangan ganjil.")

    def cek_bulat(self, bilangan):
        if bilangan.is_integer():
            print(f"{int(bilangan)} adalah bilangan bulat.")
        else:
            print(f"{bilangan} bukan bilangan bulat.")

    def hitung_faktorial(self, angka):
        faktorial = 1
        for i in range(1, int(angka) + 1):
            faktorial *= i
        return faktorial

    def main(self):
        print()
        print("="*20)
        print("Menu:")
        print("1. Cek Bilangan Ganjil")
        print("2. Cek Bilangan Bulat")
        print("3. Faktorial")
        print("4. Keluar")
        print("="*20)
        print()

        while True:
            choice = input("Masukkan pilihan (1/2/3/4): ")

            if choice == '1':
                bilangan = float(input("Masukkan bilangan: "))
                self.cek_ganjil(bilangan)
            elif choice == '2':
                bilangan = float(input("Masukkan bilangan: "))
                self.cek_bulat(bilangan)
            elif choice == '3':
                angka = int(input("Masukkan angka untuk dihitung faktorial: "))
                self.hasil_faktorial = self.hitung_faktorial(angka)
                print(f"Faktorial dari {angka} adalah {self.hasil_faktorial}")
            elif choice == '4':
                print("Terima kasih, program selesai.")
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan 1, 2, 3, atau 4.")

            keluar = input("Apakah sudah selesai? (y/n): ")
            if keluar == "y":
                isDone = False
            else:
                isDone = True

obj=Pilihan()
obj.main()
