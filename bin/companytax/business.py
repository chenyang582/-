

def main():
    a = business_income_tax(10000, 8000)
    print(a.profit)
    print(a.BusinessIncomeTax)
    print(a.aferprofit)

class business_income_tax():
    def __init__(self, sales, cost = 0, rate = 0.25):
        self.sales = sales
        self.cost = cost
        self.rate = rate
        self.profit = self.sales - self.cost    #税前利润（毛利）

#所得税税额
    @property
    def BusinessIncomeTax(self):
        if self.profit <= 0:
            return 0
        elif self.profit > 0:
            return round(self.profit * self.rate, 4)

#税后利润
    @property
    def aferprofit(self):
        return round(self.profit - self.BusinessIncomeTax)



if __name__ == '__main__':
    main()
