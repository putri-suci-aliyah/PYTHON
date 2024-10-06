class ListHapusDataKota:

    variabel_list_daftar_kota = ["Bandung", "Jakarta", "Surabaya"]

    def cetak_list_data_kota(self):
        print(self.variabel_list_daftar_kota)

    def hapus_data_kota(self, param_nama_kota):

        if param_nama_kota in self.variabel_list_daftar_kota:
            # remove digunakan untuk menghapus elemen
            self.variabel_list_daftar_kota.remove(param_nama_kota)


obj = ListHapusDataKota()
obj.cetak_list_data_kota()
print("-----SESUDAH HAPUS ELEMEN BANDUNG-----")
obj.hapus_data_kota("Bandung")
obj.cetak_list_data_kota()
