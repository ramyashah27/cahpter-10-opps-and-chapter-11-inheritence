class train:
    def __init__(self,name , fare, seats):
        self.name= name
        self.fare= fare
        self.seats = seats
    def getstatus(self):
        print(f"the name of the train is ({self.name}) \n total fare of each seat is {self.fare} \n total seats in the train is {self.seats} ")
intercity = train("intercity express : 14025",90, 400)
intercity.getstatus()       