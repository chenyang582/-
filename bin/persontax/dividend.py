

#通过红利发放
class dividend():
    def __init__(self, salary):
        self.salary = salary

#通过红利发放的税额
    def dicidendtax(self):
        amount = self.salary * 0.2
        return amount

#通过红利发放的税后到手金额
    def afterdividend(self):
        return self.salary - self.dicidendtax()
