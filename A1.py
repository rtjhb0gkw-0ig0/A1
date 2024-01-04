class FireChicken:
    
    def __init__(self, a1, a2, a3, a4, a5):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5

    def fn1(self,a1,a2):
        self.a1 = a1
        self.a2 = a2
        print("SF")
    def fn2(self,a3,a4, a5):
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        print("SF")    
    def fn3(self):
        print(self.a1, self.a2, self.a3, self.a4, self.a5)  


g_FireChicken = FireChicken(1,2,3,4,5)
g_FireChicken.fn3()
g_FireChicken.fn1(10,12)
g_FireChicken.fn2(24,32,44)
g_FireChicken.fn3()