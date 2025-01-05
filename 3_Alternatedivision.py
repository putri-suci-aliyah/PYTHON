class Alternatedivision: #name class

    #membuat method
    def cetakAlternatedivision(self):
        dividend = int(input('Please enter the number to divide: '))
        divisor = int(input('Please enter dividend: '))
        # If possible, divide them and report the result
        if divisor != 0:
            quotient = dividend / divisor
        print(dividend, '/', divisor, "=", quotient)
        print('Program finished')

#membuat object
obj = Alternatedivision()

#memanggil method melalui object
obj.cetakAlternatedivision()