
def main():
    chenyang = VerificationCollection(salary = 20000, collectrate = 0.1, social = 0, special = 0, other = 0, legal = 0)
    print(chenyang.collectrate)
    print(chenyang.income)
    print(chenyang.YearIncome)
    print(chenyang.PersonalIncomeTax())
    print(chenyang.Verificationtax())
    print(chenyang.afterVerificationtax())



class VerificationCollection():
    def __init__(self, salary, social = 0, special = 0, other = 0, legal = 0, collectrate = 0.1):
        self.salary = salary
        self._collectrate = collectrate  #应税所得率
        self.social = social
        self.special = special
        self.other = other
        self.legal = legal * 12  #月基本减除费用
        self.income = self.salary * self.collectrate #应税所得额
        self.payable = self.YearIncome - self.legal - self.YearSocial - self.YearSpecial - self.YearOther

    @property
    def collectrate(self):
        return self._collectrate

    @property
    def YearSalary(self):
        return self.salary * 12

    @property
    def YearSocial(self):
        return self.social * 12

    @property
    def YearSpecial(self):
        return self.special * 12

    @property
    def YearOther(self):
        return self.other * 12

    @property
    def YearIncome(self):
        return self.income * 12

    #生产经营所得个人所得税
    def PersonalIncomeTax(self):
#        payable = self.YearIncome - self.legal - self.YearSocial - self.YearSpecial - self.YearOther
        if self.payable <= 0:
            amount = 0
            return amount
        if self.payable > 0 and self.payable <= 30000:
            amount = self.payable * 0.05
            return amount
        elif self.payable > 30000 and self.payable <= 90000:
            amount = self.payable * 0.1 - 1500
            return amount
        elif self.payable > 90000 and self.payable <= 300000:
            amount = self.payable * 0.2 - 10500
            return amount
        elif self.payable > 300000 and self.payable <= 500000:
            amount = self.payable * 0.3 - 40500
            return amount
        elif self.payable > 500000:
            amount = self.payable * 0.35 - 65500
            return amount
        else:
            amount = -94
            return amount

    #按照年收入的税负率
    def Verificationtax(self):
        if self.salary <= 0:
            return 0
        amount = self.PersonalIncomeTax()
        rate = amount / self.YearIncome
        return rate

    #按照年开票金额的税负率
    def afterVerificationtax(self):
        if self.salary <= 0:
            return 0
        amount = self.PersonalIncomeTax()
        rate = amount / self.YearSalary
        return rate



class SpeVerificationCollection():
    def __init__(self, salary):
        self.salary = salary

    #月收入小于30000免收个人所得税，大于30000核定征收率1.5%
    def PersonalIncomeTax(self):
        if self.salary <= 30000:
            amount = 0
            return amount
        if self.salary > 30000:
            amount = self.salary * 0.015 * 12
            return amount
        else:
            amount = -93
            return amount







if __name__ == '__main__':
    main()
