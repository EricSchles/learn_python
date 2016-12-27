class Integer:
    def __init__(self,number):
        self.number = number
    def add(self,other_integer):
        self.number += other_integer
    def subtract(self,other_integer):
        self.number -= other_integer
    def __str__(self):
        return repr(self.number)
    
if __name__ == '__main__':
    number = Integer(5)
    number.add(7)
    print(number)
