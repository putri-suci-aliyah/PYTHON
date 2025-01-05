class DataSiswa:
    list_data_semua_siswa = []

    def input_list_data(self):
        while True:
            print('\n')
            print("=========================")
            print("        INPUT SISWA       ")
            print("=========================")
            dict_data_siswa = {}
            nis = input("NIS\t\t: ")
            nama = input("NAMA\t: ")
            alamat = input("ALAMAT\t: ")

            dict_data_siswa['nis'] = nis
            dict_data_siswa['nama'] = nama
            dict_data_siswa['alamat'] = alamat

            self.list_data_semua_siswa.append(dict_data_siswa)
            pilihan = input("Input data lagi (Y/T)? ")
            pilihan = pilihan.upper()
            if pilihan == 'T':
                break

    def cetak_list_data(self):
        print('\n')
        print("============================================")
        print("NIS\t\t\t\t NAMA\t\t\t ALAMAT\t")
        print("============================================")
        for data_siswa in self.list_data_semua_siswa:
            print(data_siswa['nis'] + "\t\t\t" + data_siswa['nama'] + "\t\t\t" + data_siswa['alamat'])
        print("============================================")
        print("Silahkan tekan Enter untuk kembali ke menu utama")
        input()

    def menu(self):

        while True:
            print("=========================")
            print("        MENU          ")
            print("=========================")
            print(" 1. INPUT SISWA ")
            print(" 2. DAFTAR SISWA ")
            print(" 3. KELUAR ")

            pilihan = int(input("Masukan pilihan Anda : "))

            if pilihan == 1:
                self.input_list_data()
            elif pilihan == 2:
                self.cetak_list_data()
            elif pilihan == 3:
                break
            else:
                print("Piilihan tidak ada. Silahkan tekan tombol Enter")
                input()

obj = DataSiswa()
obj.menu()