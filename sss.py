from netaddr import IPRange
def ipRangeTest(ipAddr, ipRange):
    for key, value in ipRange.items():
        if ipAddr in key:
            return value
    return 'unknown'
ipRange = { IPRange('112.65.158.42', '112.65.158.46'):'百年保险资产管理有限',
            IPRange('220.248.3.113', '220.248.3.113'):'百年保险资产管理有限',
            IPRange('220.248.3.73', '220.248.3.78'):'百年保险资产管理有限',
            IPRange('139.224.200.115', '139.224.200.115'):'百年保险资产管理有限',
            IPRange('218.24.167.24', '218.24.167.31'):'百年人寿保险股份有限公司',
            IPRange('124.93.96.64', '124.93.96.96'):'百年人寿保险股份有限公司',
            IPRange('123.177.20.130', '123.177.20.134'):'百年人寿保险股份有限公司',
            IPRange('123.177.21.37', '123.177.21.37'):'百年人寿保险股份有限公司',
            IPRange('218.24.167.27', '218.24.167.27'):'百年人寿保险股份有限公司'
            }
for _ in range(10):
           a = input("输入a.b.c.d:")
           b = input("输入{0}.b.c.d:".format(a))
           c = input("输入{0}.{1}.c.d:".format(a,b))
           d = input("输入{0}.{1}.{2}.d:".format(a,b,c))
           ipAddr = '.'.join(map(str, (a,b,c,d)))
           print(ipAddr, ipRangeTest(ipAddr,ipRange))
