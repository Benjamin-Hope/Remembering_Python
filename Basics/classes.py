# here we will look over the classes that we will use in the project

#lets define a class name car, and actually here we will define what a car should look like

class vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle #this is an attribute of the class, in this case the body style of the car

    def drive (self,speed ): #-- we define a method for when we are driving 
        self.mode = "drive"
        self.speed = speed #this is a method of the class, in this case the speed of the car

class Car(vehicle): ##here we say that the class car is a child of the class vehicle
    def __init__(self , engine): #this is the constructor of the class thats lets the python know what to do when we create an object of this class
        ##above the 'self' referes to the object that we are creating, in this case a CAR
        super().__init__("car") #this is how we call the constructor of the parent class, and we associate the body style of the car to the car object
        self.wheels = 4 #this is another attribute of the CAR   class, in this case the number of wheels
        self.doors = 5 #this is another attribute of the CAR class, in this case the number of doors
        self.engine = engine #here we say that the engine type is the engine that that was passed in as argument

    #-- we specify the methods of the class, in this case the drive method
    def drive(self, speed):
        ##we need to call again the super command to access the drive method of the parent class
        super().drive(speed)
        print("you are driving a car ",self.engine, " at speed ",speed)


## to practice lest do one for bikes 

class Bike(vehicle):
    def __init__(self,engine, sidecar):
        super().__init__("bike")
        if sidecar == "yes": #we can also use the if statement inside the classes to define the attributes of the class
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.engine = engine


#lets create an object of the class car

Ferrari = Car("V8") #here we create an object of the class car, and we pass in the engine type as an argument

print(Ferrari.bodystyle) #here we print the body style of the car
print(Ferrari.wheels) #here we print the number of wheels of the car

##we can also define functions inside the classes, these are called methods

Ferrari.drive(100) #here we call the drive method of the car class