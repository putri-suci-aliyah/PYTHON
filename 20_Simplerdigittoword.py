class Simplerdigittoword: #name class

    #membuat method
    def cetakSimplerdigittoword(self):
        # Use a mult-way conditional statement
        value = int(input())
        if value == 0:
            print("zero")
        elif value == 1:
            print("one")
        elif value == 2:
            print("two")
        elif value == 3:
            print("three")
        elif value == 4:
            print("four")
        elif value == 5:
            print("five")
        print("Done")

#membuat object
obj = Simplerdigittoword()

#memanggil method melalui object
obj.cetakSimplerdigittoword()