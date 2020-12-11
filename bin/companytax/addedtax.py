



def main():
    a = addedtax(10000)
    print(a.price)
    print(a.addedtaxvalue)
    print(a.additional.surtax())
    print(a.price + a.addedtaxvalue)
    print(a.pretax)
    print(a.all_pretax)


#companytype为0是一般纳税人，为1是小规模纳税人  halve默认不减半
class addedtax():
    def __init__(self, sales, companytype = 0, rate = 0.06, halve = False):
        self.mysales = sales
        self.mycompanytype = companytype
        self.myrate = rate
        self.additional = additional(self.addedtaxvalue, halve)

#应税销售额
    @property
    def sales(self):
        return self.mysales

    @property
    def companytype(self):
        return self.mycompanytype

    @property
    def rate(self):
        return self.myrate

#不含税价格
    @property
    def price(self):
        return round((self.sales / (1 + self.rate)), 4)

#税额
    @property
    def addedtaxvalue(self):
        return round(self.price * self.rate, 4)

#与应税销售额的税负率(不含附加税)
    @property
    def pretax(self):
        if self.sales == 0:
            return 0
        else:
            return round(self.addedtaxvalue / self.sales, 4)

#附加税的税负率
    @property
    def additional_pretax(self):
        if self.sales == 0:
            return 0
        else:
            return round(self.additional.surtax() / self.sales, 4)



#与应税销售额的税负率(含附加税)
    @property
    def all_pretax(self):
        if self.sales == 0:
            return 0
        else:
            return round((self.addedtaxvalue + self.additional.surtax()) / self.sales, 4)






class additional():
    def __init__(self, addedtaxvalue, halve = False):
        self.addedtaxvalue = addedtaxvalue
        self.halve = halve

#城市维护建设税
    @property
    def urban_construction(self):
        return self.addedtaxvalue * 0.07

#教育费附加
    @property
    def education(self):
        return self.addedtaxvalue * 0.03

#地方教育费附加
    @property
    def local_education(self):
        return self.addedtaxvalue * 0.02

    def surtax(self):
        if not self.halve:
            return self.urban_construction + self.education + self.local_education
        else:
            return (self.urban_construction + self.education + self.local_education) / 2


if __name__ == '__main__':
    main()
