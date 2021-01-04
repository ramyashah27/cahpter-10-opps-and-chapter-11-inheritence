class mc:
    company = "microsoft"

    def __init__(self,name,product):
        self.name = name
        self.product = product
    def getinfo(self):
        print(f"the name of {self.company} coder is {self.name}, nd PRODUCT IS {self.product}")
ramya = mc("ramya", "bing")
coder= mc('ayush','word')
ramya.getinfo()
coder.getinfo()















