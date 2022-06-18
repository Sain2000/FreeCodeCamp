import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        k=list(kwargs.keys())
        v=list(kwargs.values())
        self.contents=[]
        for i in range(len(k)):
            for j in range(v[i]):
                self.contents.append(k[i])
    
    def draw(self, n):
        if n>=len(self.contents):
            return self.contents
        l=[]
        for i in range(n):
            x=random.randrange(len(self.contents))
            l.append(self.contents[x])
            del self.contents[x]
        return l

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count=0
    for i in range(num_experiments):
        expected_copy=copy.deepcopy(expected_balls)
        hat_copy=copy.deepcopy(hat)
        colors_gotten=hat_copy.draw(num_balls_drawn)
        for color in colors_gotten:
            if color in expected_copy:
                expected_copy[color]-=1
        if (all(x <= 0 for x in expected_copy.values())):
            count+=1
    return count/num_experiments