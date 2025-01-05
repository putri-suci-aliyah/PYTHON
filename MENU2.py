class Pilihan:
    def main(self):
        print()
        print("="*100)
        print("Menu:")
        print("1. Cek Bilangan Ganjil")
        print("2. Cek Bilangan Bulat")
        print("3. Faktorial")
        print("4. Keluar")
        print("="*100)
        print()

        while True:
            choice = input("Masukkan pilihan (1/2/3/4): ")

            if choice == '1':
                print("Anda memilih Cek Bilangan Ganjil")
                from CekBilanganGanjil import obj
                obj.cek_ganjil()

            elif choice == '2':
                print("Anda memilih Cek Bilangan Bulat")
                from CekBilanganBulat import obj
                obj.cek_bulat()

            elif choice == '3':
                print("Anda memilih dihitung faktorial ")
                from CekHitungFaktorial import hitung_faktorial
                angka = int(input("Masukkan angka untuk menghitung faktorial: "))

                hasil_faktorial = hitung_faktorial(angka)
                print(f"Faktorial dari {angka} adalah: {hasil_faktorial}")

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
