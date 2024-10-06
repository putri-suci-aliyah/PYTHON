class SetHapusDataKota:

    variabel_set_daftar_kota = {"Jakarta","Bandung", "Jakarta", "Surabaya"}

    def cetak_set_data_kota(self):
        print(self.variabel_set_daftar_kota)

    def hapus_data_kota(self, param_nama_kota):

        if param_nama_kota in self.variabel_set_daftar_kota:
            # remove digunakan untuk menghapus elemen
            self.variabel_set_daftar_kota.remove(param_nama_kota)


obj = SetHapusDataKota()
obj.cetak_set_data_kota()
print()
print("-----SESUDAH HAPUS ELEMEN BANDUNG-----")
obj.hapus_data_kota("Bandung")
obj.cetak_set_data_kota()
