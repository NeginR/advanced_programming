from Person9812021Negin import * 
class Driver(Person):

    def __init__(self,name,busNo):
        self._busNo = busNo
        super().__init__(name)

    @property
    def busNo(self):
        return self._busNo
    
    @busNo.setter
    def busNo(self,busNo):
        self._busNo = busNo

    @property
    def name(self):
        return self._name

    def __str__(self):
        return "Driver: {}  busNo :{}".format(self._name,self._busNo)