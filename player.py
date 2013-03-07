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
	
            print "self.num is ",self.num
            if self.preferred_attrs[i]:
                if self.num > 35:
                    self.tempnum = 15;
                    num = random.randint(0,self.tempnum)
	            print "random num is",num                    

		    self.num = self.num - num - 20;
                    self.attributes[i] = 60+num+20
                else:
                    self.tempnum = self.num;
                    num = random.randint(0,self.tempnum)
                    self.num = self.num - num;
                    self.attributes[i] = 60+num
                
        for i in range(len(self.preferred_attrs)):
            if not self.preferred_attrs[i]:
                if self.num > 35:
                    self.tempnum = 35;
                    num = random.randint(0,self.tempnum)
                    self.num = self.num - num;
                    self.attributes[i] =  60+num
                else:
                    self.tempnum = self.num;
                    num = random.randint(0,self.tempnum)
                    self.num = self.num - num;
                    self.attributes[i] =  60 + num

        if self.num > 0:
            print "self.num is not used ",self.num
            for i in  range(len(self.attributes)):
                if self. num + self.attributes[i] < 95:
                    self.attributes[i] = self.attributes[i] + self.num
                    print self.attributes[i]
                    return
                else:
                    tempnum = self.attributes[i] + self.num
                    self.num = tempnum - 95
                    self.attributes[i] = 95
                
    def __str__(self):
        return self.skill + '   ' + ', '.join(str(attr) for attr in self.attributes)
        #return ', '.join(self.attributes)
        #return str(self.attributes)
        
          
def test(skill,preferred_attrs):
    p = Player(skill, preferred_attrs)
    print "preferred_attrs is ", str(preferred_attrs)
    p.make()
    print p
              
if __name__ == '__main__':
    test(skill,list1)

  
