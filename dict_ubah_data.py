class DictUbahData:

    dictionary_siswa = {
        "nik": "0001",
        "nama": "siswa 1",
        "jurusan": "ipa"
    }

    def cetak_dict_data_siswa(self):
        print(self.dictionary_siswa)

    def ubah_data_siswa(self, param_kunci, param_nilai):
        self.dictionary_siswa[param_kunci] = param_nilai

obj = DictUbahData()
obj.cetak_dict_data_siswa()
print("-----SESUDAH DIUBAH KUNCI JURUSAN DENGAN NILAI IPS-----")
obj.ubah_data_siswa("jurusan","ips")
obj.cetak_dict_data_siswa()
