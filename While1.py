class While1:
    def CetakWhile(self):
        print("Output 1: ")
        i = 1
        while i <= 10:
            print(i)
            i += 1

        print("\nOutput 2: ")
        i = 1
        while i <= 10:
            print(i, end='')
            i += 1

        print("\nOutput 3: ")
        i = 1
        while i <= 10:
            print(i, end=' ')
            i += 1

        print("\nOutput 4: ")
        i = 1
        while i <= 10:
            print(i, end=' ')
            i +=2

        print("\nOutput 5: ")
        i = 2
        while i <= 10:
            print(i, end=' ')
            i +=2

        print("\nOutput 6: ")
        i = 10
        while i >= 1:
            print(i, end=' ')
            i = i-1


obj = While1()
obj.CetakWhile()
