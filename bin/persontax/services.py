

def main():
    chenyang = services(3000)
    print(chenyang.type)
    print(chenyang.income)
    print(chenyang.Withholding())
    print(chenyang.Aftertax())



class services():
    def __init__(self, salary, type = '劳务报酬所得'):
        self.salary = salary
        self.type = type
        self.income = self.Getincome()    #应纳税所得额

#    @property
#    def type(self):
#        return self.type

#劳务报酬所得、稿酬所得、特许权使用费所得以收入减除百分之二十的费用后的余额为收入额。稿酬所得的收入额减按百分之七十计算。
    def Getincome(self):
        if self.type == '劳务报酬所得':
            myincome = self.salary * 0.8
            return myincome
        elif self.type == '稿酬所得':
            myincome = self.salary * 0.8 * 0.7
            return myincome
        elif self.type == '特许权使用费所得':
            myincome = self.salary * 0.8
            return myincome
        else:
            myincome = -98
            return myincome

#计算预扣预缴款
    def Withholding(self):

        if self.salary <= 0:
            return 0

        if self.salary > 0 and self.salary <= 800:
            incomed = 0
        elif self.salary > 800 and self.salary <= 4000:
            incomed = self.salary - 800
        elif self.salary > 4000:
            incomed = self.salary * 0.8
        else:
            incomed = -97

        if self.type ==  '稿酬所得':
            incomed = incomed * 0.7

        if incomed >= 0 and incomed <= 20000:
            amount = incomed * 0.2
            return amount
        elif incomed > 2000 and incomed <= 50000:
            amount = incomed * 0.3 - 2000
            return amount
        elif incomed > 50000:
            amount = incomed * 0.4 - 7000
            return amount
        else:
            amount = -96
            return amount

#计算预扣预缴后的实际到手金额
    def Aftertax(self):
        if self.salary <= 0:
            return 0

        amount = self.Withholding()
#        print(amount)
        tax = self.salary - amount
        return tax

if __name__ == '__main__':
    main()
