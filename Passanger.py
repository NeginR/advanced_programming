from Person9812021Negin import * 
class Passanger(Person):

    def __init__(self,name,seat,busNo):
        self._seat = seat
        self._busNo = busNo
        super().__init__(name)

    @property
    def seat(self):
        return self._seat
    
    @seat.setter
    def seat(self,seat):
        self._seat = seat


    def __str__(self):
        return "Passangr: {} seat : {} busNo :{}".format(self._name,self._seat,self._busNo)