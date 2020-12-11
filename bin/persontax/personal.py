


def main():
    chenyang = Wages(21000, 1698.92, 3500)
    print(chenyang.salary)
    print(chenyang.YearSalary)
    print(chenyang.PersonalIncomeTax())
    print(chenyang.pretax())
    print(chenyang.aftertax())
    print(chenyang.afterincome())


class Wages():
    def __init__(self, salary, social, special, other = 0):
        self.salary = salary   #税前收入
        self.social = social   #社保公积金
        self.__LEGAL = 60000   #年基本减除费用
        self.special = special #专项扣除
        self.other = other     #其他，暂时不用
        self.payable = self.YearSalary - self.__LEGAL - self.YearSocial - self.YearSpecial - self.YearOther  #应纳税所得额

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




    #计算年度个人所得税
    def PersonalIncomeTax(self):
#        payable = self.YearSalary - self.__LEGAL - self.social - self.YearSpecial - self.YearOther
        if self.payable <= 0:
            amount = 0
            return amount
        elif self.payable > 0 and self.payable <= 36000:
            amount = self.payable * 0.03 - 0
            return amount
        elif self.payable > 36000 and self.payable <= 144000:
            amount = self.payable * 0.1 - 2520
            return amount
        elif self.payable > 144000 and self.payable <= 300000:
            amount = self.payable * 0.2 - 16920
            return amount
        elif self.payable > 300000 and self.payable <= 420000:
            amount = self.payable * 0.25 - 31920
            return amount
        elif self.payable > 420000 and self.payable <= 660000:
            amount = self.payable * 0.30 - 52920
            return amount
        elif self.payable > 660000 and self.payable <= 960000:
            amount = self.payable * 0.35 - 85920
            return amount
        elif self.payable > 960000:
            amount = self.payable * 0.45 - 181920
            return amount
        else:
            amount = -99
            return amount

#计算税前税负率
    def pretax(self):
        if self.salary <= 0:
            return 0
        amount = self.PersonalIncomeTax()
        rate = amount / (self.salary * 12)
        return rate


#计算税后税负率
    def aftertax(self):
        if self.salary <= 0:
            return 0
        amount = self.PersonalIncomeTax()
        rate = amount / (self.salary * 12 - self.social * 12)
        return rate

#计算税后到手金额
    def afterincome(self):
        if self.salary <= 0:
            return 0
        amount = self.PersonalIncomeTax()
        return self.YearSalary - self.YearSocial - amount








if __name__ == '__main__':
    main()
