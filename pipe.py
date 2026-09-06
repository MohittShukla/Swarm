import random
from config import CANVAS_WIDTH,HEIGHT

class Pipe:
        def __init__(self):
            self.x = random.randint(10,CANVAS_WIDTH - 10)
            self.y = random.randint(10,HEIGHT - 10)
            self.length = random.randint(10,150)
            self.thickness = random.randint(1,6) 

        def copy(self):
            new_pipe = Pipe()
            new_pipe.x = self.x
            new_pipe.y = self.y
            new_pipe.thickness = self.thickness
            new_pipe.length = self.length
            return new_pipe
        
        def mutate(self):
             choice = random.choice(['x','y','thickness','length'])
             is_frog_jump = random.random() < 0.05

             if choice == 'x':
                value = random.randint(-8,8)
                self.x += value
                floor = 10
                ceil = CANVAS_WIDTH - 10
                if is_frog_jump:
                  self.x = random.randint(floor,ceil)
                  return True
                else:
                  self.x = max(floor,min(self.x,ceil))

             elif choice == 'y':
                value = random.randint(-8,8)
                self.y += value
                floor = 10
                ceil = HEIGHT - 10
                if is_frog_jump:
                  self.y = random.randint(floor,ceil)
                  return True
                else:
                  self.y = max(floor,min(self.y,ceil))


             elif choice == 'thickness':
                value = random.randint(-1,1)
                self.thickness += value
                floor = 1
                ceil = 10
                self.thickness = max(floor,min(self.thickness,ceil))

             else:
                value = random.randint(-12,12)
                self.length += value
                floor = 10
                ceil = 200
                self.length = max(floor,min(self.length,ceil))
             return False



