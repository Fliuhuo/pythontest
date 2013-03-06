# receive: recv
# description: desc
# level: lvl, lv

import random
import sys

class Player:
    def __init__(self, skill, preferred_attrs=[]):
        self.attribute = [60,60,60,60,60]
        self.num = 80
        self.skill = skill
        self.preferred_attrs = preferred_attrs
        
    def make(self):
        self.tempnum = 0
        for i in range(5):
            if(self.preferred_attrs[i]  == 1):
                if self.num > 35:
                    self.tempnum = 15;
                    num = random.randint(0,self.tempnum)
                    self.num = self.num - num - 20;
                    self.attribute[i] = 60+num+20
                else:
                    self.tempnum = self.num;
                    num = random.randint(0,self.tempnum)
                    self.num = self.num - num;
                    self.attribute[i] = 60+num

                
                
        for i in range(5):
            if(self.preferred_attrs[i]  == 0):
                if self.num > 35:
                    self.tempnum = 35;
                    num = random.randint(0,self.tempnum)
                    self.num = self.num - num;
                    self.attribute[i] =  60+num
                else:
                    self.tempnum = self.num;
                    num = random.randint(0,self.tempnum)
                    self.num = self.num - num;
                    self.attribute[i] =  60+num
                
                
    def printself(self):
        for i in range(5):
            print self.skill
            print self.attribute[i];
          
          
def test():
    skill = 'test'
    preferred_attrs = [ 0, 1, 0, 1, 0]
    if len(sys.argv) >= 3:
       skill = sys.argv[1]
       preferred_attrs=sys.argv[2]

    p = Player(skill, preferred_attrs)
    p.make()
    p.printself(); 
              
if __name__ == '__main__':
    test()

  