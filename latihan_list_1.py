list_nama_kota = []

# 1A
print()
print("-"*50)
list_nama_kota.append("Serang")
list_nama_kota.append("Jakarta")
list_nama_kota.append("Padang")
list_nama_kota.append("Semarang")
list_nama_kota.append("Yogyakarta")
list_nama_kota.append("Palembang")
list_nama_kota.append("Surabaya")
print(list_nama_kota)

# 1B
print("-"*50)
len(list_nama_kota)
print("Jumlah elemen:", len(list_nama_kota))

# 1C
print("-"*50)
list_nama_kota = str(input("Masukkan nama kota: "))
if "Semarang" in list_nama_kota:
    print("ADA")
else:
    print("TIDAK ADA")

# 1D
print("-"*50)
kota = ['Serang', 'Jakarta', 'Padang', 'Semarang', 'Yogyakarta', 'Palembang', 'Surabaya']
index = kota.index("Palembang")
print("Palembang berada pada indeks ke: ",index)

# 1E
print("-"*50)
kota = ['Serang', 'Jakarta', 'Padang', 'Semarang', 'Yogyakarta', 'Palembang', 'Surabaya']
kota.clear()
print("",kota)