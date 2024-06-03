class Vehicle:
    def __init__(self,make,color):
        self.make=make
        self.color=color
        
    def accelerate(self):
        print("Acceleration start")
        
    def hoot(self):
        print("honk honk")
        
class Bus(Vehicle):
    def __init__(self,make,color,passengers):
        super().__init__(make,color)
        self.passengers=passengers
        
    def start_boarding(self):
        print("THe bus is boarding")
        
class Lorry(Vehicle):
    def __init__(self,make,color,max_load):
         super().__init__(make,color)
         self.max_load=max_load
        
    def unload(self):
        print("unloading")
        
   