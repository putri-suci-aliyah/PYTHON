class Boolvars: #name class
    #deklarasi atribute
    a = True
    b = False

    #membuat method
    def cetakBoolvars(self):
        print('a =', self.a, ' b =', self.b)
        self.a = False
        print('a =', self.a, ' b =', self.b)

#membuat object
obj = Boolvars()

#memanggil method melalui object
obj.cetakBoolvars()