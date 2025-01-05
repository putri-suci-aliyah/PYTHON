class Betterdivision: #name class

    dividend = 0
    divisor = 0
    #membuat method
    def cetakBetterdivision(self):
        print('Please enter two numbers to divide.')
        dividend = int(input('Please enter the first number to divide: '))
        divisor = int(input('Please enter the second number to divide: '))
        # If possible, divide them and report the result
        if divisor != 0:
            print(dividend, '/', divisor, "=", dividend / divisor)

#membuat object
obj = Betterdivision()

#memanggil method melalui object
obj.cetakBetterdivision()