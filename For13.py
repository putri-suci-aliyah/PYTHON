class For13:
    def CetakFor(self):
        input_number = 6
        for i in range(1, input_number + 1):
            print("Current Number is :", i, " and the cube is", (i * i * i))
obj = For13()
obj.CetakFor()

nilai_list = []

print("=========== BACA data ===========")
for i in range(5):
    nilai = input("Nama kota: ", i+1)
    nilai_list.append(nilai)
print("Nama kota ke 1 adalah ",nilai_list)
