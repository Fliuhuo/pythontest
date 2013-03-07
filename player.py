# receive: recv
# description: desc
# level: lvl, lv

import random
import sys

class Player:
    def __init__(self, skill, preferred_attrs=[]):
        self.attributes = [60,60,60,60,60]
        self.num = 80
        self.skill = skill
        self.preferred_attrs = preferred_attrs
        
    def make(self):
        self.tempnum = 0
        for i in range(len(self.preferred_attrs)):
            if self.preferred_attrs[i] == True:
                if self.num > 35:
                    self.tempnum = 15;
                    num = random.randint(0,self.tempnum)
                    self.num = self.num - num - 20;
                    self.attributes[i] = 60+num+20
                else:
                    self.tempnum = self.num;
                    num = random.randint(0,self.tempnum)
                    self.num = self.num - num;
                    self.attributes[i] = 60+num
                
        for i in range(len(self.preferred_attrs)):
            if self.preferred_attrs[i] == False:
                if self.num > 35:
                    self.tempnum = 35;
                    num = random.randint(0,self.tempnum)
                    self.num = self.num - num;
                    self.attributes[i] =  60+num
                else:
                    self.tempnum = self.num;
                    num = random.randint(0,self.tempnum)
                    self.num = self.num - num;
                    self.attributes[i] =  60+num

        if self.num > 0:
            for attr in  self.attributes:
                if num + attr < 95:
                    attr = attr + num
                    return
                else:
                    tempnum = attr+num
                    num = tempnum - 95
                    attr = 95
                
    def __str__(self):
        return self.skill + '   ' + ', '.join(str(attr) for attr in self.attributes)
        #return ', '.join(self.attributes)
        #return str(self.attributes)
        
          
def test():
    skill = 'test'
    preferred_attrs = [ True, True, False, True, False]
    if len(sys.argv) >= 3:
       skill = sys.argv[1]
       preferred_attrs=sys.argv[2]

    p = Player(skill, preferred_attrs)
    p.make()
    print p
              
if __name__ == '__main__':
    test()

  
