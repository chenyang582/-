
from persontax.verification import VerificationCollection
from win import Toplevel1
import tkinter as tk
from decimal import Decimal
from companytax.addedtax import addedtax
from companytax.business import business_income_tax
from company import company
from tkinter import *
from companytax.stamp import stamp

def main():
    global root
    root = tk.Tk()
    global top
    top = Toplevel1 (root)
    top.Button1.configure(command = caltax)
    top.Button2.configure(command = deleteall)
    top.menubar.add_command(label="使用说明",command = infodisplay)
    deleteall()
    root.mainloop()


#传入一个数字，输出文本格式且保留两位小数的数字
def quantize(number):
    str_number = str(number)
    str_number = Decimal(str_number).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")
    return str_number


def caltax():

    if not test():
        deleteentry()
        return 1

    a = round(float(top.Entry1.get()), 2)  #平台公司开具的金额数
    b = round(float(top.Entry1_3.get()), 2)  #个体户数
    c = round(float(top.Entry1_4.get()), 2)  #每户开票金额数
    d = top.v1.get()    #所得税税点
    e = top.v2.get()    #增值税专票税点
    f = top.v3.get()    #个体户开具普通发票和专用发票，0为普票 1为专票
    g = top.v4.get()    #核定征收率
    h = top.v5.get()    #总包合同印花税
    i = top.v6.get()    #分包合同印花税


    #计算单个个体户的增值税和不含税价格
    myaddedtax = addedtax(c, 1, 0.03, True)
    myprice = myaddedtax.price            #不含税价格
    myaddedtaxvalue = myaddedtax.addedtaxvalue  #增值税税额
    mysurtax = quantize(myaddedtax.additional.surtax())  #附加税税额
    alladdedtaxvalue = myaddedtax.addedtaxvalue + myaddedtax.additional.surtax()  #总税额
    myall_pretax = quantize(myaddedtax.all_pretax * 100)

    #计算印花税
    mystamp = stamp(c, True, i)
    mystamptax = mystamp.stamptax
#    print('{} {} {}'.format(c, i, mystamp.stamptax))
    print15 = '个体户一般来说需要签订分包合同缴纳印花税，个体户按50%减半征收。单个个体户需要缴纳印花税{}*{}%={}元。\n'.format(quantize(c), quantize(i*100/2),quantize(mystamptax) )

    #开普票才能进行增值税减免
    if f == 0:
        if c <= 1200000:
    #计算单个个体户的个人所得税,小于30万时免征增值税，所以价税合计金额合并计算所得税
            myVerificationCollection = VerificationCollection(salary = c/12, collectrate = g, social = 0, special = 0, other = 0, legal = 0)
            simtax = myVerificationCollection.PersonalIncomeTax() + mystamptax    #单个个体户的税金总和
            #单个个体户的税负率
            if c == 0:
                simtaxrate = 0
            else:
                simtaxrate = (simtax) / c
            alltax = simtax * b    #所有个体户的税金总和汇总
            myaddeddeduction = 0
            allmycost = c * b    #所有个体户的总成本
            allmyaddeddeduction = myaddeddeduction * b  #所有个体户的总进项抵扣
            print2 = '按照国家规定，小规模纳税人年度销售额未超120万元的免征增值税。单个个体户的年开票金额未超过120万，按照免增值税进行测算。个体户全年经营收入为价税金额合计。\n'
            print3 = '单个个体户需要缴纳增值税0元，需要缴纳附加税0元。\n'
            print4 = '单个个体户的核定征收率为{}%，假设个体户全年经营收入为{}元，缴纳个人所得税{}元。\n'.format(g * 100, quantize(c), quantize(myVerificationCollection.PersonalIncomeTax()))
            print5 = '单个个体户的增值税、附加税、个人所得税、印花税总税负成本为{}元，税负率为{}%。所有个体户的总税负成本为{}元。\n'.format(quantize(simtax), quantize(simtaxrate * 100),quantize(alltax))
        elif c > 1200000:
            myVerificationCollection = VerificationCollection(salary = myprice/12, collectrate = g, social = 0, special = 0, other = 0, legal = 0)
            simtax = myVerificationCollection.PersonalIncomeTax() + alladdedtaxvalue + mystamptax  #单个个体户的税金总和
            #单个个体户的税负率
            if c == 0:
                simtaxrate = 0
            else:
                simtaxrate = (simtax) / c
            alltax = simtax * b   #所有个体户的税金总和汇总
            myaddeddeduction = 0  #普通发票没有进项税额抵扣
            allmycost = c * b    #所有个体户的总成本
            allmyaddeddeduction = myaddeddeduction * b  #所有个体户的总进项抵扣
            print2 = '按照国家规定，小规模纳税人年度销售额未超120万元的免征增值税。单个个体户的年开票金额超过120万，按照需要缴纳增值税进行测算（征收率为3%）。个体户全年经营收入为不含税销售金额合计。\n'
            print3 = '单个个体户需要缴纳增值税{}-{}/(1+{})={}元，附加税减半征收，需要缴纳附加税{}*6%={}元。\n'.format(quantize(c), quantize(c), '3%', quantize(myaddedtaxvalue), quantize(myaddedtaxvalue), mysurtax)
            print4 = '单个个体户的核定征收率为{}%，假设个体户全年经营收入为{}元，需要缴纳个人所得税{}元。\n'.format(g * 100, quantize(c), quantize(myVerificationCollection.PersonalIncomeTax()))
            print5 = '单个个体户的增值税、附加税、个人所得税、印花税总税负成本为{}元，税负率为{}%。所有个体户的总税负成本为{}元。\n'.format(quantize(simtax), quantize(simtaxrate * 100), quantize(alltax))
        print1 = '由于个体工商户开出为增值税普通发票，所以平台公司将没有增值税进项税额进行增值税抵扣。平台公司的记账成本为个体户的价税合计金额，每个个体户的价税合计金额为{}元。\n'.format(quantize(c))
    elif f == 1:
        myVerificationCollection = VerificationCollection(salary = myprice/12, collectrate = g, social = 0, special = 0, other = 0, legal = 0)
        simtax = myVerificationCollection.PersonalIncomeTax() + alladdedtaxvalue + mystamptax   #单个个体户的税金总和
        #单个个体户的税负率
        if c == 0:
            simtaxrate = 0
        else:
            simtaxrate = (simtax) / c
        alltax = simtax * b   #所有个体户的税金总和汇总
        myaddeddeduction = myaddedtaxvalue  #专用发票可以进行进项税额抵扣
        allmycost = myprice * b    #所有个体户的总成本
        allmyaddeddeduction = myaddeddeduction * b  #所有个体户的总进项抵扣
        print2 = '按照国家规定，小规模纳税人年度销售额未超120万元的免征增值税，但是开具增值税专用发票不享受免征增值税政策。所以按照需要缴纳增值税进行测算（征收率为3%）。个体户全年经营收入为不含税销售金额合计。\n'
        print3 = '单个个体户需要缴纳增值税{}-{}/(1+{})={}元，附加税减半征收，需要缴纳附加税{}*6%={}元。\n'.format(quantize(c), quantize(c), '3%', quantize(myaddedtaxvalue), quantize(myaddedtaxvalue), mysurtax)
        print4 = '单个个体户的核定征收率为{}%，假设个体户全年经营收入为{}元，需要缴纳个人所得税{}元。\n'.format(g * 100, quantize(c), quantize(myVerificationCollection.PersonalIncomeTax()))
        print5 = '单个个体户的增值税、附加税、个人所得税、印花税总税负成本为{}元，税负率为{}%。所有个体户的总税负成本为{}元。\n'.format(quantize(simtax), quantize(simtaxrate * 100), quantize(alltax))
        print1 = '由于个体工商户开出为增值税专用发票（征收率为3%），所以平台公司将获得增值税进项税额进行抵扣。单个个体户可获得进项税额{}元。平台公司的记账成本为个体户的不含税销售金额，每个个体户的不含税销售金额为{}元。\n'.format(quantize(myaddeddeduction), quantize(myprice))


    #计算企业所有进项的印花税
    mycompanystamp = stamp(c, False, i)
    companystamptax = mycompanystamp.stamptax * b


    mycompany = company(sales = a, addedrate = e, incomerate = d, stamprate = h, ahalve = False, shalve = False, addeddeduction = allmyaddeddeduction, cost = allmycost, incomestamptax = companystamptax)

    print6 = '由于平台公司需要开出增值税专用发票，所以平台公司均为一般纳税人。需要缴纳增值税、附加税、企业所得税、印花税。不享受附加税和印花税减半优惠。\n'
    print16 = '平台公司需要缴纳的印花税一般包括总包项目印花税和分包项目印花税，其中总包合同印花税{}元，所有分包合同印花税{}元（全额征收），总计{}元。\n'.format(quantize(mycompany.outcomestamptax), quantize(companystamptax), quantize(mycompany.mystamptax))
    #根据个体户是否开户专票，平台公司的记账成本将不同。
    if f == 0:
        print7 = '由于个体户开具普通发票，平台公司将没有进项税额。平台公司的记账成本为所有个体户的价税合计金额和平台公司附加税、印花税，所有个体户的价税合计金额为{}*{}={}元。\n'.format(quantize(c),quantize(b),quantize(allmycost))
    elif f == 1:
        print7 = '由于个体户开具专用发票，平台公司将获得所有个体户的进项税额{}*{}={}元，平台公司的记账成本为所有个体户的不含税销售金额和平台公司附加税、印花税，所有个体户的不含税销售金额为{}*{}={}元。\n'.format(quantize(myaddeddeduction),quantize(b),allmyaddeddeduction,quantize(myprice),quantize(b),quantize(allmycost))

    print8 = '平台公司增值税销项税额{}-{}/(1+{})={}元，增值税缴纳金额为销项-进项={}元\n'.format(quantize(a), quantize(a), quantize(e), quantize(mycompany.myaddedtax.addedtaxvalue), quantize(mycompany.myaddedtaxvalue))
    print9 = '平台公司需要缴纳附加税{}*12%={}元。\n'.format(quantize(mycompany.myaddedtaxvalue), quantize(mycompany.myadditional))
    print10 = '平台公司不含税收入为{}元，记账成本为{}元（附加税及印花税可记为成本），毛利润为{}元。\n'.format(quantize(mycompany.myaddedtax.price), quantize(mycompany.mybusiness_income_tax.cost),quantize(mycompany.mybusiness_income_tax.profit))
    print11 = '平台公司需要缴纳企业所得税{}*{}={}元，税后净利润为{}元。\n'.format(quantize(mycompany.mybusiness_income_tax.profit), quantize(d), quantize(mycompany.myBusinessIncomeTax),quantize(mycompany.myaferprofit))
    print12 = '平台公司的增值税、附加税、企业所得税、印花税总税负成本为{}元，总税负率为{}%。\n'.format(quantize(mycompany.alltax), quantize(mycompany.allcompanypretax * 100))


    #公司和个人的总税负额
    allplatformtax = mycompany.alltax + alltax

    #公司包税和不包税下的盈利情况
    if mycompany.myaferprofit >= 0:
        print13 = '平台公司为盈利状态，'
        if mycompany.myaferprofit - alltax >= 0:
            allprofit = mycompany.myaferprofit - alltax    #包个税下的利润
            print14 = '并且包个体户的税后仍然为盈利状态（即平台公司将代个体户缴纳增值税及个人所得税、印花税），包税后剩余利润为{}元。\n'.format(quantize(allprofit))
        else:
            allprofit = mycompany.myaferprofit - alltax
            print14 = '但是包个体户的税后就变成亏损状态（即平台公司将代个体户缴纳增值税及个人所得税、印花税），包税后剩余利润为{}元。\n'.format(quantize(allprofit))
    elif mycompany.myaferprofit < 0:
        allprofit = mycompany.myaferprofit - alltax
        print13 = '平台公司为亏损状态，如果包个体户的税亏损将更严重（即平台公司将代个体户缴纳增值税及个人所得税、印花税），包税后剩余利润为{}元。\n'.format(quantize(allprofit))
        print14 = ''

    top.Text1.configure(state='normal')
    top.deletetext()
    top.Text1.insert('insert', '个体工商户的税负情况：\n', "tag_1")
    top.Text1.insert('insert', print1)
    top.Text1.insert('insert', '***********************************\n' )
    top.Text1.insert('insert', print15)
    top.Text1.insert('insert', '***********************************\n' )
    top.Text1.insert('insert', print2)
    top.Text1.insert('insert', print3)
    top.Text1.insert('insert', print4)
    top.Text1.insert('insert', print5, "tag_2")
    top.Text1.insert('insert', '*********************************************\n' )
    top.Text1.insert('insert', '\n' )
    top.Text1.insert('insert', '*********************************************\n' )
    top.Text1.insert('insert', '平台公司的税负情况：\n', "tag_1")
    top.Text1.insert('insert', print6)
    top.Text1.insert('insert', '***********************************\n' )
    top.Text1.insert('insert', print16)
    top.Text1.insert('insert', '***********************************\n' )
    top.Text1.insert('insert', print7)
    top.Text1.insert('insert', print8)
    top.Text1.insert('insert', print9)
    top.Text1.insert('insert', print10)
    top.Text1.insert('insert', print11, "tag_2")
    top.Text1.insert('insert', print12, "tag_2")
    top.Text1.insert('insert', '***********************************\n' )
    top.Text1.insert('insert', '平台公司的盈利分析：\n', "tag_1")
    top.Text1.insert('insert', print13, "tag_2")
    top.Text1.insert('insert', print14, "tag_2")
    top.Text1.configure(state='disabled')



def deleteall():
    top.Text1.configure(state='normal')
    top.deleteentry2()
    top.deletetext()

    top.Text1.insert('insert', '金财互联平台（SZ002530），通过打造智慧化的财税服务新体验，帮助企业实现“合规、降负、增利”，致力于提升小微企业主的获得感和幸福感。\n')
    top.Text1.insert('insert', '***********************************\n' )
    top.Text1.insert('insert', '本模型主要用于类众包平台公司税负成本和经营利润的测算，可用于税务筹划、灵活用工、金财云商下等多种场景下的税负成本测算。\n')
    top.Text1.insert('insert', '***********************************\n' )
    top.Text1.insert('insert', '本模型测算中个体工商户均采用核定征收模式，个体工商户的个人所得税适用生产经营所得的个人所得税税率。\n')
    top.Text1.insert('insert', '***********************************\n' )
    top.Text1.insert('insert', '本模型由个人开发，数据未经过严格测试，故可能存在BUG或错漏，演示数据仅供参考。如您发现问题请联系开发者进行软件修正和更新（微信号Near-river）。\n' , "tag_2")
    top.Text1.insert('insert', '***********************************\n' )
    top.Text1.insert('insert', '如您对金财互联智慧税筹解决方案感兴趣，请联系金财互联销售人员，金财互联税筹专家团队将竭诚为您提供专业、可靠、贴心的税筹服务。\n' )
    top.Text1.configure(state='disabled')



def t_close_handler():
    root.attributes("-disabled", 0)
    f1.destroy()


def infodisplay():
    root.attributes("-disabled", 1)
    global f1
    f1 = Toplevel(root)
    # f1.config(width=710,height=510)
    f1.geometry("997x214+417+205")                             #("671x182+287+246")
    f1.title("平台型公司税负及盈利情况测模型")
    f1.resizable(0, 0)
    f1.protocol("WM_DELETE_WINDOW", t_close_handler)
    Text1 = Text(f1)
    #Label_1 = Label(f1)
    Text1.place(relx=0.04, rely=0.093, relheight=0.794, relwidth=0.937)
    Text1.configure(background="#d9d9d9")
    Text1.configure(state='normal')
    Text1.insert('insert', '平台型公司税负及盈利情况模型由金财互联陈阳个人制作，软件可自由散发使用。\n')
    Text1.insert('insert', '该模型未经过严格测试，故仅供参考。开发者不承担因数据不准确引发的任何问题。\n')
    Text1.insert('insert', '如您发现模型存在问题或与开发者交流，欢迎您添加微信号Near-river与软件开发者联系。感谢您的使用！！\n')
    Text1.insert('insert', '***********************************\n' )
    Text1.insert('insert', 'V1.0版本说明（20201103）：\n')
    Text1.insert('insert', '软件发布\n')
    Text1.insert('insert', 'V1.1版本说明（20201106）：\n')
    Text1.insert('insert', '考虑了印花税的情形，增加了总包合同和项目合同的印花税点选，并根据点选在计算过程中加入印花税。\n')
    Text1.insert('insert', 'V1.2版本说明（20201104）：\n')
    Text1.insert('insert', '修正了计算附加税金额的BUG。\n')
    #Text1.configure(text='''说明：个税税筹计算器由陈阳个人制作，软件可自由散发使用。\n该计算器数据未经过严格测试，故仅供参考。开发者不承担因数据不准确引发的任何问题。\n如您发现软件存在问题或与开发者交流，欢迎您添加微信号Near-river与作者联系。''')
    Text1.configure(state='disabled')
    scrol = Scrollbar(f1)
    scrol.pack(side="right", fill="y")
    Text1.configure(yscrollcommand = scrol.set)
    scrol.configure(command=Text1.yview)


def test():
    try:  # 如果能运行float(s)语句,继续
        float(top.Entry1.get())
        pass
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        return False
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        int(top.Entry1_3.get())
        pass
    except ValueError:
        return False
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(top.Entry1_4.get())
        pass
    except ValueError:
        return False

    if float(top.Entry1.get()) < 0:
        return False
    elif int(top.Entry1_3.get()) < 0:
        return False
    elif float(top.Entry1_4.get()) < 0:
        return False
    elif float(top.Entry1.get()) > 10000000:
        return False
    elif int(top.Entry1_3.get()) > 10000:
        return False
    elif float(top.Entry1_4.get()) > 10000000:
        return False
    return True


def deleteentry():

    top.Entry1.delete(0, "end")
    top.Entry1.insert(0,'0')

    top.Entry1_3.delete(0, "end")
    top.Entry1_3.insert(0,'1')

    top.Entry1_4.delete(0, "end")
    top.Entry1_4.insert(0,'0')

    tk.messagebox.showerror('输入错误提示', '不能输入文字或者负数呀，并且个体户必须是整数，不然怎么计算…')


if __name__ == '__main__':
    main()
