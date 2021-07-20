from Passanger9812021Negin import *
from Driver9812021Negin import *
class Bus:
    
    #make constructor for Bus
    def __init__(self,busNo,driverName,arrivalTime,departureTime,begginig,destination,capacity=32,masafat=100):
        
        self._busNo=busNo
        self._driver=Driver(driverName,self._busNo)

        #self._arrivalTime=(arrivalTime%24)*arrivalTime
        #self._departureTime=(departureTime%24)*departureTime
        """temp = departureTime.split(":")
        if isinstance(temp[0],(int,float)) and isinstance(temp[1],(int,float)):
            temp[0] = temp[0] % 24
            temp[1] = temp[1] % 60
            self._departureTime = temp[0] + " : "+temp[1]
        else:
            self._departureTime = "01:00
        temp = arrivalTime.split(":")
        if isinstance(temp[0],(int,float)) and isinstance(temp[1],(int,float)):
            temp[0] = temp[0] % 24
            temp[1] = temp[1] % 60
            self._arrivalTime = temp[0] + " : "+temp[1]
        else:
            self._arrivalTime = "00:00"
    """
        temp = departureTime.split(":") 
        temp[0] = int(temp[0]) % 24
        temp[1] = int(temp[1]) % 60
        self._departureTime = str(temp[0]) + " : " +str(temp[1])
        temp = arrivalTime.split(":")
        temp[0] = int(temp[0]) % 24
        temp[1] = int(temp[1]) % 60
        self._arrivalTime = str(temp[0]) + " : " +str(temp[1])
        self._begginig=begginig
        self._masafat = masafat
        self._destination=destination
        self._capacity=capacity
        self._seatNumberList=[0 for x in range(capacity)]
        self._reservedSeat = 0
        self._passangers = []
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def busNo(self):
        return self._busNo

    @property
    def reservedSeat(self):
        return self._reservedSeat

    @reservedSeat.setter
    def reservedSeat(self,reservedSeat):
        self._reservedSeat = reservedSeat

    #reservation Part   
    def reserveSeat(self,seatNumber,passangerName):
        
        if self._seatNumberList[seatNumber-1] == 0:
            
            self._seatNumberList[seatNumber-1]=passangerName
            self._passangers.append(Passanger(passangerName,seatNumber,self._busNo))
            self._reservedSeat+=1

            return True,self._passangers[-1]
        
        return False,False
    
    #show all empty seat
    def _showAllEmptySeat(self):
        
        for i in range(self.capacity):
            if self._seatNumberList[i] == 0:
                print(i+1,"Have n't been reserved yet")
            else:
                print(i+1,"The seat was reserved by {}".format(self._seatNumberList[i]))
    
    #🙎‍♂️show feature of chair by chart
    def _showByChart(self): 
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("chart of Seat in bus")
        
        for i in range(self.capacity):
            if self._seatNumberList[i] == 0:
                print("o", end="")
            else:
                print("x", end="")

        
        print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n")
        

    #show feature of bus and show char for seating in bus
    def show(self):
        self._showAllEmptySeat()
        self._showByChart()
    
    def showAvailable(self):
        if self._capacity - self._reservedSeat != 0:
            print("\nThe bus : {} with driver's name: {} \n  arrival time: {} \t departure Time : {} \n begginig at : {} \n destination : {}\n masafat :{} \n capacity :{}\n rezerved seat :{} \n".format(self._busNo,self._driver.name,self._arrivalTime,self._departureTime,self._begginig,self._destination,self._masafat,self._capacity,self._reservedSeat))
            print("Ja dare:)")
    
    #make string with all the elements:)
    def __str__(self): 
        return "\nThe bus : {} with driver's name: {} \n  arrival time: {} \t departure Time : {} \n begginig at : {} \n destination : {}\n masafat :{} \n capacity :{}\n rezerved seat :{} \n".format(self._busNo,self._driver.name,self._arrivalTime,self._departureTime,self._begginig,self._destination,self._masafat,self._capacity,self._reservedSeat)
        