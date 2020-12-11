

#计算全年一次性奖金收入，注意2022年1月1日起不再适用
def main():
    chenyang = AnnualBonus(130000)
    print(chenyang.salary)
    print(chenyang.AnnualIncomeTax())
    print(chenyang.AfterAnnualIncome())

class AnnualBonus():
    def __init__(self, salary):
        self.salary = salary

#计算具体的税金
    def AnnualIncomeTax(self):
        if self.salary <= 0:
            return 0
        monthsalary = round(self.salary / 12, 2)
        if monthsalary > 0 and monthsalary <= 3000:
            amount = self.salary * 0.03
            return amount
        elif monthsalary > 3000 and monthsalary <= 12000:
            amount = self.salary * 0.1 - 210
            return amount
        elif monthsalary > 12000 and monthsalary <= 25000:
            amount = self.salary * 0.2 - 1410
            return amount
        elif monthsalary > 25000 and monthsalary <= 35000:
            amount = self.salary * 0.25 - 2660
            return amount
        elif monthsalary > 35000 and monthsalary <= 55000:
            amount = self.salary * 0.3 - 4410
            return amount
        elif monthsalary > 55000 and monthsalary <= 80000:
            amount = self.salary * 0.35 - 7160
            return amount
        elif monthsalary > 80000:
            amount = self.salary * 0.45 - 15160
            return amount
        else:
            amount = -95
            return amount


#计算税后到手金额
    def AfterAnnualIncome(self):
        amount = self.AnnualIncomeTax()
        return self.salary - amount

#计算税负率
    def pretax(self):
        if self.salary <= 0:
            return 0
        amount = self.AnnualIncomeTax()
        rate = amount/self.salary
        return rate


if __name__ == '__main__':
    main()
