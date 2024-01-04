class FireChicken:
    def __init__(self, a1, a2, a3, a4, a5):#初始化數值
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5

    def fn1(self,a1,a2):#設定a1~a2的數值
        self.a1 = a1
        self.a2 = a2
        print("SF")
    def fn2(self,a3,a4,a5):#設定a3~a5的數值
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        print("SF")    
    def fn3(self):#輸出所有數值
        print(self.a1, self.a2, self.a3, self.a4, self.a5) 

print("g_FireChicken_1:")
g_FireChicken_1 = FireChicken(1,2,3,4,5)
g_FireChicken_1.fn3()#輸出所有數值
g_FireChicken_1.fn1(10,12)#設定a1~a2的數值
g_FireChicken_1.fn2(24,32,44)#設定a3~a5的數值
g_FireChicken_1.fn3()#輸出所有數值
print("g_FireChicken_2:")
g_FireChicken_2 = FireChicken(5,4,3,2,1)
g_FireChicken_2.fn3()#輸出所有數值
g_FireChicken_2.fn1(151,141)#設定a1~a2的數值
g_FireChicken_2.fn2(354,456,985)#設定a3~a5的數值
g_FireChicken_2.fn3()#輸出所有數值
print("g_FireChicken_3:")
g_FireChicken_3 = FireChicken(5,4,3,2,1)
g_FireChicken_3.fn3()#輸出所有數值
g_FireChicken_3.fn1(884,635)#設定a1~a2的數值
g_FireChicken_3.fn2(125,25,35)#設定a3~a5的數值
g_FireChicken_3.fn3()#輸出所有數值
print("g_FireChicken_4:")
g_FireChicken_4 = FireChicken(10,22,46,35,51)
g_FireChicken_4.fn3()#輸出所有數值
g_FireChicken_4.fn1(58,14)#設定a1~a2的數值
g_FireChicken_4.fn2(54,75,25)#設定a3~a5的數值
g_FireChicken_4.fn3()#輸出所有數值