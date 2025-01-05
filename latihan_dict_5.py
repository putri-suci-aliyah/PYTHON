list_data_semua_siswa = []
while True:
    print('\n')
    dict_data_siswa = {}
    nis = input("NIS\t\t: ")
    nama = input("NAMA\t: ")# LENGKAPI UNTUK INPUT NAMA
    alamat = input("ALAMAT\t: ")# LENGKAPI UNTUK INPUT ALAMAT

    dict_data_siswa['nis'] = nis
    dict_data_siswa['nama'] = nama
    dict_data_siswa['alamat'] = alamat
    # LENGKAPI UNTUK MENGINPUTKAN VARIABEL nama, alamat
    list_data_semua_siswa.append(dict_data_siswa)
    pilihan = input("Input data lagi (Y/T)? ")
    pilihan = pilihan.upper()
    if pilihan == 'T':
        break
print("============================================")
print("NIS\t\t\t NAMA\t\t ALAMAT\t")
print("============================================")
for data_siswa in list_data_semua_siswa:
    print(data_siswa['nis'] + "\t\t\t" + data_siswa['nama'] + "\t\t\t" + data_siswa['alamat']) # LENGKAPI UNTUK MENAMPILKAN nama, alamt
print("============================================")