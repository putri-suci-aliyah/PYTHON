class ListUbahDataKota:

    variabel_list_daftar_kota = ["Bandung", "Jakarta", "Surabaya"]

    def cetak_list_data_kota(self):
        print(self.variabel_list_daftar_kota)

    def ubah_data_kota(self, param_nama_kota, param_nama_kota_baru):

        if param_nama_kota in self.variabel_list_daftar_kota:
            indeks = self.variabel_list_daftar_kota.index(param_nama_kota)
            self.variabel_list_daftar_kota[indeks] = param_nama_kota_baru



obj = ListUbahDataKota()
obj.cetak_list_data_kota()
print("-----SESUDAH MERUBAH BANDUNG MENJADI PALEMBANG-----")
obj.ubah_data_kota("Bandung","Palembang")
obj.cetak_list_data_kota()