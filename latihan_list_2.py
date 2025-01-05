list_bilangan_bulat = [11, 8, -90, -5, 0, 1, 4, -10, 11, 1, 43]
print()
# 2A
print("-"*100)
print("Bilangan terkecil adalah : ",min(list_bilangan_bulat))
print("Bilangan terbesar adalah : ",max(list_bilangan_bulat))

# 2B
print("-"*100)
list_bilangan_bulat.sort()
print("Urutan nilai dari terkecil hingga terbesar: ",list_bilangan_bulat)

list_bilangan_bulat.reverse()
print("Urutan nilai dari terbesar hingga terkecil: ",list_bilangan_bulat)

# 2C
print("-"*100)
jumlah_11 = list_bilangan_bulat.count(11)
jumlah_minus90 = list_bilangan_bulat.count(-90)

print("Jumlah nilai/elemen 11 sebanyak: ",jumlah_11)
print("Jumlah nilai/elemen -90 sebanyak: ",jumlah_minus90)
print("-"*100)