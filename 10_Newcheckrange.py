class Newcheckrange: #Name Class

    #Membuat methode
    def cetakNewcheckrange(self):

        value = int(input("Please enter an integer value in the range 0...10: "))
        if value >= 0 and value <= 10:  # Only one, slightly more complicated check
             print("In range")
        print("Done")

#membuat object
obj = Newcheckrange()

#memanggil method melalui object
obj.cetakNewcheckrange()