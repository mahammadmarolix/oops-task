#SINGLE INHERITANCE
class parent:
    def __init__(self):
        self.name = "Naguru mahammad"
        print(self.name)
    def m1(self):
        print("parent class")
class child(parent):
    def m2(self):
        print("child class")
e = child()
e.m1()
e.m2()


#MULTILEVEL INHERITANCE
class fruits:
    def __init__(self):
        self.name = "apple"
        print(self.name)
    def m1(self):                                                                 
        print("this is an apple")                                                                                       # 
class grape(fruits):                                                  
    def m2(self):
        print("grape is also fruit")
class mango(grape):
    def m3(self):
        print("mango is also fruit")
e = mango()
e.m1()
e.m2()
e.m3()


#multiple inheritnce
class vegetables:
    def __init__(self):
        self.name = "tomato"
        print(self.name)                                   
    def m1(self):
        print("This is a base class of veg")
class leafs:
    def m2(self):
        self.name = "curry leaf"
        print(self.name)
        print("this is sub class of leafs")
class vegetarian(vegetables, leafs):
    def m3(self):
        print("this is multiple of all class")
e = vegetarian()
e.m1()
e.m2()
e.m3()

#herarical inhertance
class chef:
    def __init__(self):
        self.name = "Naguru mahammad"
        print(self.name)
    def m1(self):
        print("best chef ever in chef class")
class servent(chef):
    def m2(self):
        print("excellent servent class")
class cleaner(chef):                                     
    def m3 (self):
        print("best cleaner class")
e = cleaner()
e.m1()
e.m3()
m = servent()
m.m2()
m.m1()



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

