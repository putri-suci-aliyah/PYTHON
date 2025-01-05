class Absvalueconditional: #name class

    #membuat method
    def cetakAbsvalueconditional(self):
        # Acquire a number from the user and print its absolute value.
        n = int(input("Enter a number: "))
        print('|', n, '| = ', (-n if n < 0 else n), sep='')


#membuat object
obj = Absvalueconditional()

#memanggil method melalui object
obj.cetakAbsvalueconditional()