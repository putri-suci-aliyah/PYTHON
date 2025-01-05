class Floatequals2: #name class

    #membuat method
    def cetakFlotequels2(self):
        d1 = 1.11 - 1.10
        d2 = 2.11 - 2.10
        print('d1 =', d1, ' d2 =', d2)
        if -0.0000001 < d1 - d2 < 0.0000001:
            print('Same')
        else:
            print('Different')

#membuat object
obj = Floatequals2()

#memanggil method melalui object
obj.cetakFlotequels2()