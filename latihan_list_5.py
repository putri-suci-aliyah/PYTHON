class DataKota:
    list_data_kota = []

    def input_list_data(self):

        while True:
            print('\n')
            print("=========================")
            print("        INPUT LIST       ")
            print("=========================")
            data = input("Data kota : ")
            self.list_data_kota.append(data)

            pilihan = str(input("Apakah ingin input data lagi Y/T : "))
            if pilihan.upper() == 'T':
                break

    def cari_list_data(self):
        while True:
            print('\n')
            print("=========================")
            print("        CARI DATA        ")
            print("=========================")
            data = input("Cari Data kota : ")

            if data in self.list_data_kota:
                print(data, ' terdapat pada list')
            else:
                print(data, ' tidak terdapat pada list')

            pilihan = str(input("Apakah ingin input cari data lagi Y/T : "))
            if pilihan.upper() == 'T':
                break

    def hapus_list_data(self):
        while True:
            print('\n')
            print("=========================")
            print("        HAPUS DATA       ")
            print("=========================")
            data = input("Hapus Data kota : ")

            if data in self.list_data_kota:
                print(data, ' sudah dihapus dari list')
                self.list_data_kota.remove(data)
            else:
                print(data, ' tidak terdapat pada list')

            pilihan = str(input("Apakah ingin input hapus data lagi Y/T : "))
            if pilihan.upper() == 'T':
                break

    def cetak_list_data(self):
        print('\n')
        print("=========================")
        print("        DAFTAR LIST      ")
        print("=========================")

        indeks = 1
        for val in self.list_data_kota:
            print(indeks, '.', val)
            indeks += 1

        print('=========================')
        print("Silahkan tekan Enter untuk kembali ke menu utama")
        input()

    def menu(self):

        while True:
            print("=========================")
            print("        PILIHAN          ")
            print("=========================")
            print(" 1. INPUT LIST DATA ")
            print(" 2. DAFTAR LIST DATA ")
            print(" 3. CARI LIST DATA ")
            print(" 4. HAPUS LIST DATA")
            print(" 5. KELUAR ")

            pilihan = int(input("Masukan pilihan Anda : "))

            if pilihan == 1:
                self.input_list_data()
            elif pilihan == 2:
                self.cetak_list_data()
            elif pilihan == 3:
                self.cari_list_data()
            elif pilihan == 4:
                self.hapus_list_data()
            elif pilihan == 5:
                break
            else:
                print("Piilihan tidak ada. Silahkan tekan tombol Enter")
                input()


obj = DataKota()
obj.menu()
