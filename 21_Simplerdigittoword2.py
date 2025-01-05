class Simplerdigittoword2: #name class

    #membuat method
    def cetakSimplerdigittoword2(self):
        value = int(input())
        if value == 0:
            print("zero")
        if value == 1:
            print("one")
        if value == 2:
            print("two")
        if value == 3:
            print("three")
        if value == 4:
            print("four")
        if value == 5:
            print("five")
        print("Done")


#membuat object
obj = Simplerdigittoword2()

#memanggil method melalui object
obj.cetakSimplerdigittoword2()