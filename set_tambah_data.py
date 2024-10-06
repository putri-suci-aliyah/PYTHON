class SetTambahDataKota:

    variabel_set_daftar_kota = {"Bandung", "Jakarta", "Bandung", "Surabaya"}

    def tambah_data_kota(self, param_nama_kota):
        # add digunakan untuk menambah elemen nama kota
        self.variabel_set_daftar_kota.add(param_nama_kota)

    def cetak_list_data_kota(self):
        print(self.variabel_set_daftar_kota)


obj = SetTambahDataKota()
obj.cetak_list_data_kota()
print("-----SESUDAH DITAMBAHKAN ELEMEN BARU-----")
obj.tambah_data_kota("Semarang")
obj.tambah_data_kota("Yogyakarta")
obj.tambah_data_kota("Yogyakarta")
obj.cetak_list_data_kota()
