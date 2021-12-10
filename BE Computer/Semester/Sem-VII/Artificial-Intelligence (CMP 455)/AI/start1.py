class maximum:
    def assign(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def maxim(self):
        if self.num1>self.num2:
            self.maxi = self.num1
            # return self.num1

        else:
            self.maxi = self.num2

            # return self.num2
    def printer(self):
        print(self.maxi, "is greater")


m = maximum()
m.assign(6,7)
m.maxim()
m.printer()

# a = m.maxim()
# m.printer(a)