class Betterfeedback: #name class

    #membuat method
    def cetakBetterfeedback(self):
        dividend = int(input('Please enter the number to divide: '))
        divisor = int(input('Please enter dividend: '))
        # If possible, divide them and report the result
        if divisor != 0:
            print(dividend, '/', divisor, "=", dividend / divisor)
        else:
            print('Division by zero is not allowed')

#membuat object
obj = Betterfeedback()

#memanggil method melalui object
obj.cetakBetterfeedback()