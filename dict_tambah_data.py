class DictTambahData:

    dictionary_siswa = {
        "nik": "0001",
        "nama": "siswa 1"
    }

    def cetak_dict_data_siswa(self):
        print(self.dictionary_siswa)

    def tambah_data_siswa(self, param_kunci, param_nilai):
        self.dictionary_siswa[param_kunci] = param_nilai

obj = DictTambahData()
obj.cetak_dict_data_siswa()
print("-----SESUDAH DITAMBAHKAN KUNCI DAN ELEMEN BARU-----")
obj.tambah_data_siswa("jurusan","ipa")
obj.tambah_data_siswa("usia",17)
obj.cetak_dict_data_siswa()
