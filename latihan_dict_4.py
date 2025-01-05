list_data_siswa = [] # LIST data siswa
dict_siswa_satu = {} # DICTIONARY SISWA SATU
dict_siswa_satu['nis'] = '2024001'
dict_siswa_satu['nama'] = 'Siswa 1'
dict_siswa_satu['alamat'] = 'Jl. Jakarta No. 1 Bandung'
list_data_siswa.append(dict_siswa_satu) # APPEND DICTIONARY KE LIST
dict_siswa_dua = {} # DICTIONARY SISWA DUA
dict_siswa_dua['nis'] = '2024002'
dict_siswa_dua['nama'] = 'Siswa 2'
dict_siswa_dua['alamat'] = 'Jl. Stasiun Timur No. 1 Bandung'
list_data_siswa.append(dict_siswa_dua) # APPEND DICTIONARY KE LIST
print("="*70)
print("NIS\t\t\t Nama\t\t Alamat\t")
print("="*70)
for val in list_data_siswa:
    print(val['nis'] + "\t\t" + val['nama'] + "\t\t" + val['alamat'])
print("="*70)