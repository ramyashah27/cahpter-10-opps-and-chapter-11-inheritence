#self refers to the instance of the class
# it is automatically passed with a fuction called call from an object
import time
class employee:
    clock=time.ctime()
    company= "google"
    naam="9.02.56"
    def getsalary(self,out):
        print(f'salary is {self.salary}' )
        print(f"company is {self.job}")
        
        print(out)
    # @staticmethod
    def clockw(self):
        print(f"the time is {self.clock}")
    @staticmethod
    def wishme():
        print('continue from ,',employee.naam)
ramya= employee()
ramya.salary='1cr'
ramya.job='coder ,chessplayer,phodiee '
ramya.getsalary('bbye')
ramya.clockw()

employee.naam
ramya.wishme()
# employee.getsalary(ramya)
