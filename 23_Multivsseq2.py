class Multivsseq2: #name class

    #membuat method
    def cetakMultivsseq2(self):
        num = int(input("Enter a number: "))
        if num == 1:
            print("You entered one")
        if num == 2:
            print("You entered two")
        if num > 5:
            print("You entered a number greater than five")
        if num == 7:
            print("You entered seven")
        else:
            print("You entered some other number")

#membuat object
obj = Multivsseq2()

#memanggil method melalui object
obj.cetakMultivsseq2()