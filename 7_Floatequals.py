class Floatequals: #name class

    #membuat method
    def cetakFlotequels(self):
        d1 = 1.11 - 1.10
        d2 = 2.11 - 2.10
        print('d1 =', d1, ' d2 =', d2)
        diff = d1 - d2          # Compute difference
        if diff < 0:            # Compute absolute value
            diff = -diff
        if diff < 0.0000001:    # Are the values close enough?
            print('Same')
        else:
            print('Different')

#membuat object
obj = Floatequals()

#memanggil method melalui object
obj.cetakFlotequels()