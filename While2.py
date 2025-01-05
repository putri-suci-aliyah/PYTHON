class While2:
    def CetakWhile(self):
        num = 75869
        count = 0
        while num != 0:
            # floor division
            # to reduce the last digit from number
            num = num // 10

            # increment counter by 1
            count = count + 1
        print("Total digits are:", count)

obj = While2()
obj.CetakWhile()
