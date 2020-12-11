from companytax.addedtax import addedtax, additional
from companytax.business import business_income_tax
from companytax.stamp import stamp


def main():
    a = company(10000)
    print(a.myaddedtaxvalue)
    print(a.myadditional)
    print(a.myBusinessIncomeTax)
    print(a.alltax)
    print(a.allcompanypretax)
    print(a.myaferprofit)

#ahalve附加税是否减半征收， shalve印花税是否减半征收
#incomestamptax所有分包合同的印花税汇总
class company():
    def __init__(self, sales, addedrate = 0.06, incomerate = 0.25, stamprate = 0.001, ahalve = False, shalve = False, addeddeduction = 0, cost = 0, incomestamptax = 0):
        self.sales = sales
        self.outcomestamptax = stamp(sales, shalve, stamprate).stamptax    #总包合同印花税
        self.incomestamptax = incomestamptax                              #分包合同印花税
        self.mystamptax = self.outcomestamptax + self.incomestamptax #印花税的总和
#        self.mystamptax = self.mystamp.stamptax     #印花税的税额
        self.myaddedtax = addedtax(sales, companytype = 0, rate = addedrate, halve = ahalve)     #销项增值税
        self.addeddeduction = addeddeduction #增值税进项税金，可用于抵扣
#        self.myaddedtaxvalue = self.myaddedtax.addedtaxvalue - self.addeddeduction  #增值税税额
        self.natadditional = additional(self.myaddedtaxvalue)            #计算附加税，附加税以缴纳的增值税税额为基准
        self.myadditional = self.natadditional.surtax()                  #附加税税额
        self.mybusiness_income_tax = business_income_tax(self.myaddedtax.price, cost = cost + self.myadditional + self.mystamptax, rate = incomerate) #附加税、印花税可以计入成本
        self.myBusinessIncomeTax = self.mybusiness_income_tax.BusinessIncomeTax         #所得税税额
        self.alltax = round(self.myaddedtaxvalue + self.myadditional + self.myBusinessIncomeTax + self.mystamptax, 4)  #总税额
#        self.allcompanypretax = round(self.alltax / sales, 4)                              #总税负率
        self.myaferprofit = self.mybusiness_income_tax.aferprofit     #税后利润

    #缴纳的增值税税额
    @property
    def myaddedtaxvalue(self):
        if self.myaddedtax.addedtaxvalue - self.addeddeduction > 0:
            return self.myaddedtax.addedtaxvalue - self.addeddeduction
        elif self.myaddedtax.addedtaxvalue - self.addeddeduction <= 0:
            return 0

    @property
    def allcompanypretax(self):
        if self.sales <= 0:
            return 0
        elif self.sales > 0:
            return round(self.alltax / self.sales, 4)



if __name__ == '__main__':
    main()
