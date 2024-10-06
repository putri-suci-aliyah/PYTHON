class ListTambahDataKota:

    variabel_list_daftar_kota = ["Bandung", "Jakarta", "Surabaya"]

    def tambah_data_kota(self, param_nama_kota):
        # append digunakan untuk menambah elemen nama kota
        self.variabel_list_daftar_kota.append(param_nama_kota)

    def cetak_list_data_kota(self):
        print(self.variabel_list_daftar_kota)


obj = ListTambahDataKota()
obj.cetak_list_data_kota()
print("-----SESUDAH DITAMBAHKAN ELEMEN BARU-----")
obj.tambah_data_kota("Semarang")
obj.tambah_data_kota("Yogyakarta")
obj.cetak_list_data_kota()
