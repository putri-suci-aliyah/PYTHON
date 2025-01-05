class Samedifferent: #name class

    #membuat method
    def cetakSamedifferent(self):
        d1 = 1.11 - 1.10
        d2 = 2.11 - 2.10
        print('d1 =', d1, ' d2 =', d2)
        if d1 == d2:
            print('Same')
        else:
            print('Different')

#membuat object
obj = Samedifferent()

#memanggil method melalui object
obj.cetakSamedifferent()