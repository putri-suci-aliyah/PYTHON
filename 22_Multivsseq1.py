class Multivsseq1: #name class

    #membuat method
    def cetakMultivsseq1(self):
        num = int(input("Enter a number: "))
        if num == 1:
            print("You entered one")
        elif num == 2:
            print("You entered two")
        elif num > 5:
            print("You entered a number greater than five")
        elif num == 7:
            print("You entered seven")
        else:
            print("You entered some other number")

#membuat object
obj = Multivsseq1()

#memanggil method melalui object
obj.cetakMultivsseq1()