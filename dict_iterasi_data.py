class DictIterasiData:

    dictionary_siswa = {
        "nik": "0001",
        "nama": "siswa 1",
        "jurusan": "ipa",
        "usia": 17
    }

    def cetak_dict_data_siswa(self):
        for kunci, nilai in self.dictionary_siswa.items():
            print('Kunci : ', kunci, " memiliki nilai : ", nilai)

obj = DictIterasiData()
obj.cetak_dict_data_siswa()