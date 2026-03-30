#The topics will include OOP class design and managing object state(5pts), encapsulation(5pts), methods(5pts),  and instantiation(5pts with main loop). Following the naming conventions for functions, variables and classes; as well as appropriately placed comments(5pts) are expected.

#Creation of a class
#"__" - private attribute that ahs to be acesses through getters and setters
class SmartDevice:
    def __init__(self ,device_id,is_on,base_power_draw):
        self.__device_id=device_id
        self.__is_on=is_on
        self.__base_power_draw=base_power_draw
    
    #getters and setters for the attributes
    def get_id(self):
        return self.__device_id
    def get_ison(self):
        return self.__is_on
    def get_power(self):
        return self.__base_power_draw
    def set_id(self,id):
        self.__device_id=id
    def set_ison(self):
        self.__is_on=True
    def set_isoff(self):
        self.__is_on=False
    def set_power(self,amount):
        self.__base_power_draw=max(0,amount) #cat be less than 0
    #behaviours of a classes obejcts, METHODS THEY DO WITH THE USE OF THIER VALUES
    def toggle_power(self):
        if self.get_ison()==True:
            self.set_isoff() #switches power on and off
           
        else: 
            self.set_ison()

    def get_current_usage(self):
        if self.get_ison()==True:
            return self.get_power()
        else:
            return 0 #returns 0watt  when device is not used

#Instantiation of 3 objects for a created class, objects have defined values for attributes that can be used in methods of class
tv=SmartDevice(101,True,65)
Fan=SmartDevice(102,True,20)
Speaker=SmartDevice(103,True,10)
#Counting power usage
power_usage=0

x=input("Do you want to test your devices? y/n: ").lower()

#Running test to turn off TV and calculate total power usage
if x=="y":
    print("Current Devices status: ")
    print(tv.get_id(), tv.get_power(), tv.get_ison()) #acesses the classes info
    print(Fan.get_id(), Fan.get_power(), Fan.get_ison())
    print(Speaker.get_id(), Speaker.get_power(), Speaker.get_ison())

    #turn off power of TV that will set usage to 0watt
    print("First test:")
    tv.toggle_power()
    print(f"Turning off TV power ...... . TV _power_on: {tv.get_ison()}") 

    print(tv.get_id(), tv.get_power(), tv.get_ison()) #acesses the classes info
    print(Fan.get_id(), Fan.get_power(), Fan.get_ison())
    print(Speaker.get_id(), Speaker.get_power(), Speaker.get_ison())

    one=tv.get_current_usage()
    two=Fan.get_current_usage()
    three=Speaker.get_current_usage()
    #calcualte total usage
    power_usage= one+two+three
    print(power_usage)
else:
    print("No testing of devices, all devices are on")




        