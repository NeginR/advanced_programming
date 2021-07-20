from BusClass982021Negin import *
class Reserve:
    
    

    def __init__(self,buses=[]):
        self._buses = buses

#    @property
#    def numberEntered(self):
#        return self._numberEntered
    
#    @numberEntered.setter
#    def numberEnetered(self,numberEntered):
#        self._numberEntered = numberEntered
    
    @property
    def buses(self):
        return self._buses
    @buses.setter
    def buses(self,buses):
        self._buses = buses

    #Exit    
    def exit(self) :
        print("Thank you!\nHAvE A NICE DAY!")
        
    

    #show Reserve Bus
    def showReserveBus(self,buses):
        
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
                
                if seatNumberEntered > bus.capacity or seatNumberEntered<1:
                    print("Really Sorry!We don't have this seat number!")
                
                else:
                    freeBusSeat,passangerInfo = bus.reserveSeat(seatNumberEntered,passangerNameEntered)
                    
                    if freeBusSeat == True :
                        print(passangerInfo)
                
                    else:
                        print("Really Sorry!This seat number was reserved later!")
                break    
        if temp == 0 :
            
            print("Bus {} doesn't available !".format(busNumber))
    #show all Buses
    def showAllBuses(self,buses):
        
        print("Please Enter  Bus No:")
        busNumber = int(input())

        print("############################################################")
        for i in range(len(buses)):
            if buses[i].busNo == busNumber :
                print(buses[i])
                buses[i].show()
                break
    #show all Chairs    
    def showesChair(self,buses):
        print("############################################################")
        for i in range(len(buses)):
            print(buses[i])

      

    #input Feautur for Bus  
    def inputBusFeature(self):


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

        print("Masafat?")
        masafat = int(input())
        
        return Bus(busNoEntered,driverNameEnetred,arriavalTimeEnetred,departureTimeEntered,beggingEntered,destination,capacity,masafat)

    def checkBus(self,buses,bus):
        
        for i in range(len(buses)):
            if buses[i].busNo == bus.busNo:
                return False
        return True
            
    #new Bus    
    def makeNewBus(self,buses) :
        bus = self.inputBusFeature()
        checkIfHave = self.checkBus(buses,bus)
        if checkIfHave == True :
            self._buses.append(bus)
            print(buses[-1])
            print("Added succesfully")

        else:
            print("NO!Ma Darim Ino!Boro!")
    
    #show buses
    def showEmpty(self,buses):
        for i in range(len(buses)):
            buses[i].showAvailable()

    def numberEnteredFunc(self,numberEnetred):
        if numberEnetred == 0:
            exit()
        if numberEnetred == 1:
            self.makeNewBus(self._buses)
        elif numberEnetred == 2:
            self.showReserveBus(self._buses)
        elif numberEnetred == 3:
            self.showAllBuses(self._buses)
        elif numberEnetred == 4:
            self.showesChair(self._buses)
        elif numberEnetred == 5:
            self.showEmpty(self._buses)
        else:
            print("NO!")
    
    #ReserveNote
    @staticmethod
    def start():
        print("************************************************************\n")

        print("Enter:1----->Install")

        print("Enter:2----->Reservation")

        print("Enter:3------>show")

        print("Enter:4------>Buse ")

        print("Enter:5------->Buses Available")

        print("Enter:0------>Exit")

        print("\n*************************************************************")