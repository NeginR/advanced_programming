from BusClass982021Negin import *
from ReservationClass9812021Negin import *



#################################################################################################################################################################

if __name__ =="__main__":

    r = Reserve()
    while True :
        Reserve.start()
        n=int(input())
        r.numberEnteredFunc(n)
        if n == 0:
            break    
    
    print("BYE BYE!")

##########################################################################################################################################################################
        
"""
#Bus(busNoEntered,driverNameEnetred,arriavalTimeEnetred,departureTimeEntered,beggingEntered,destination,capacity)
class Bus:
    
    #make constructor for Bus
    def __init__(self,busNo,driverName,arrivalTime,departureTime,begginig,destination,capacity=32):
        
        self._busNo=busNo
        self._driverName=driverName
        self._arrivalTime=arrivalTime
        self._departureTime=departureTime
        self._begginig=begginig
        self._destination=destination
        self._capacity=capacity
        self._seatNumberList=[0 for x in range(capacity)]
        self._freeSeat = 0

    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def busNo(self):
        return self._busNo

        
    #reservation Part   
    def reserveSeat(self,seatNumber,passangerName):
        
        if self._seatNumberList[seatNumber-1] == 0:
        
            self._seatNumberList[seatNumber-1]=passangerName
            self._freeSeat+=1

            return True
        return False
    
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
    
    #make string with all the elements:)
    def __str__(self):
        return "The bus : {} with driver's name: {} \n  arrival time: {} \t departure Time : {} \n begginig at : {} \n destination : {} \n capacity :{}".format(self._busNo,self._driverName,self._arrivalTime,self._departureTime,self._begginig,self._destination,self._capacity)

buses=[]
def start():
    print("************************************************************\n")

    print("Enter:1----->Install")

    print("Enter:2----->Reservation")

    print("Enter:3------>show")

    print("Enter:4------>Buse Available")

    print("Enter:0------>Exit")

    print("\n*************************************************************\n")
    

#input Feautur for Bus  
def inputBusFeature():


    print("Please Enter bus's Number :")
    busNoEntered = int(input())
    
    print("Please Enetr driver's Name :")
    driverNameEnetred = input()
    
    print("Please Enetr Arrival Time :")
    arriavalTimeEnetred = input()    
    
    print("Please Enetr departure Time :")
    departureTimeEntered = input()   
    
    print("Please Enetr begginig place :")
    beggingEntered = input()
    
    print("Please Enter distination :")
    destination = input()
    
    print("Please Enter capacity :")
    capacity = int(input())


    return Bus(busNoEntered,driverNameEnetred,arriavalTimeEnetred,departureTimeEntered,beggingEntered,destination,capacity)


a=1
b=1

while  a == b :
    
    start()
    
    numberEnetred=int(input())
    
    #Exit    
    if numberEnetred == 0 :
        print("Thank you!\nHAvE A NICE DAY!")
        break
    
    #new Bus    
    if numberEnetred == 1 :
    
        buses.append(inputBusFeature())
        print("here1")
        print(buses[-1])
        print("Added succesfully")    

    if numberEnetred == 2 :
        
        temp = 0 
        print("Please Enter Bus Number:")

        busNumber=int(input())
        
        for bus in buses :
            
            if bus.busNo == busNumber :
                
                temp = 1
                print("Please Enter  Seat Number :")
                seatNumberEntered = int(input())
                print("Please Enter Passanger's Name :")
                passangerNameEntered = input()
                
                if seatNumberEntered >= bus.capacity :
                    print("Really Sorry!We don't have this seat number!")
                
                else:
                    freeBusSeat = bus.reserveSeat(seatNumberEntered,passangerNameEntered)
                
                    if freeBusSeat == True :
                        print("Passanger {} reserves {} in {} bus .".format(seatNumberEntered,passangerNameEntered,busNumber))
                
                    else:
                        print("Really Sorry!This seat number was reserved later!")
                break    
        if temp == 0 :
            
            print("Bus {} doesn't available !".format(busNumber))

    if numberEnetred == 3 :
        
        print("Please Enter  Bus No:")
        busNumber = int(input())

        print("############################################################")
        for i in range(len(buses)):
            if buses[i].busNo == busNumber :
                print(buses[i])
                print(buses[i].show())
                break

    if numberEnetred == 4:
        print("############################################################")
        for i in range(len(buses)):
            print(buses[i])
            
"""