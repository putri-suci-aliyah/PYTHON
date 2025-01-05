nama_kota = []

print("======= BACA DATA =======")
for i in range(5):
    data = input("Nama kota: ")
    nama_kota.append(data)
print()
print("======= CETAK DATA =======")
for i in range(5):
    print("Nama kota ke", i+1, "adalah", nama_kota[i])