class Checkrange: #name class

    # membuat method
    def cetakCheckrange(self):

        value = int(input("Please enter an integer value in the range 0...10: "))
        if value >= 0:       # First check
            if value <= 10:  # Second check
                print("In range")
        print("Done")

#membuat object
obj = Checkrange()

#memanggil method melalui object
obj.cetakCheckrange()