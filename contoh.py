class MenghitungBanyakData:
    def cekSets(self):
        intSet = set()
        self.number = int(input("Masukkan banyaknya elemen  : "))
        for i in range(1, self.number+1):
            value = int(input("Masukkan %d nilai    : " %i))
            intSet.add(value)

        print("Gabungan sets       : ", intSet)
        intSetLenght = len(intSet)
        print("Banyak data         : ", intSetLenght)

obj = MenghitungBanyakData()
obj.cekSets()
