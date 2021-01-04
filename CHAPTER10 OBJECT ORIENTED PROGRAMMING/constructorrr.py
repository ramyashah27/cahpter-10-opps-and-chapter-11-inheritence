class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
        print(f"ticket is{self.ticket}")
    def __init__(self):
        print('ramya shah is a good boy')

RamyaApplication.name = "ramya"
RamyaApplication.train = "Rajdhani Express"
RamyaApplication.ticket = " Ce2 "
RamyaApplication.printData()
