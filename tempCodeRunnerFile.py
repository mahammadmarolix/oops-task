#hybird inheritance
class Naguru:
    def __init__(self):
        self.name = "NAGURU"
    def m1(self):
        print("This is a surname :",self.name)
class owner(Naguru):
    def __init__(self):
        self.name = "Naguru mahaboob basha"
        super().__init__()
    def m2(self):
        print("This is a owner name:", self.name)
class wife(Naguru):
    def __init__(self):
        self.name = "Dastagiramma"
        super().__init__()
    def m3(self):
        print("This is a owner wife name :",self.name)
class son(owner, wife):
    def __init__(self):
        super().__init__()
    def m4(self):
        print("This is full info about my family ")
a = son()
a.m1()
a.m2()
a.m3()
a.m4()