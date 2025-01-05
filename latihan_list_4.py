list_data_provinsi = [
    ["1", "Bandung", "Jawa Barat"],
    ["2", "Semarang", "Jawa Tengah"],
    ["3", "Surabaya", "Jawa Timur"]
    ]

# 2A
print()
for kota in list_data_provinsi:
  print(kota)
print()

# 2B
print("="*100)
print ("Data indeks ke 1 adalah ", list_data_provinsi[1])

# 2C
print("="*100)
print()
provinsi = [
    ["Jawa Barat", "Bandung"],
    ["Jawa Tengah", "Semarang"],
    ["Jawa Timur", "Surabaya"]
]
for i in range(len(provinsi)):
    print("Provinsi", provinsi[i][0], "ibu kotanya :", provinsi[i][1])