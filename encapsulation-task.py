#encapsulation is a combination of variables and methods in a single unit
## using public acces modifiers
class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def method(self):
        self.rollno = 2024 
        print("roll num:", self.rollno)

obj = student("Naguru mahammad",2024)
obj.method()
print("Name:", obj.name)

## using private access modifiers
class employee():
    def __init__(self,name,emp_id):
        self.__name = name
        self.__emp_id = emp_id
    def display(self):
        
        print("emp ID:", self.__emp_id)
        print("Name:", self.__name)

obj = employee("das", 2018)
obj.display()

## using protected accsess modifiers

class company():
    def __init__(self,name,branch):
        self._name = name
        self._branch = branch

    def method(self):
        self._name = "Marolix"
        self._branch = "Hyderabad"
        print("company name:",self._name)
        print("main branch:", self._branch)

obj = company('marolix','hyderabad')
obj.method()
        