

def main():
    mystamp = stamp(10000)
    print(mystamp.stamptax)




#halve默认不减半
class stamp():
    def __init__(self, sales, halve = False, rate = 0.001):
        self.sales = sales
        self.rate = rate
        self.halve = halve

    @property
    def stamptax(self):
        if not self.halve:
            return round(self.sales * self.rate, 4)
        else:
            return round((self.sales * self.rate) / 2, 4)


if __name__ == '__main__':
    main()
