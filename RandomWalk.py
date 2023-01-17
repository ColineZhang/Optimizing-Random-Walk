from random import choice
from numpy import linspace
class RandomWalk:

    def __init__(self, start=[0,0], destination=[10,10], boundary=(0,50)):
        
        self.destination = destination
        self.x_values = [start[0]]
        self.y_values = [start[1]]
        self.step_numbers = len(self.x_values)
        self.boundary = linspace(boundary[0],boundary[1],boundary[1]+1)
        self.fill_walk()
    def fill_walk(self):
        while self.x_values[-1] != self.destination[0] or self.y_values[-1] != self.destination[1]:
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:
                continue
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            if x not in self.boundary or y not in self.boundary:
              continue
            self.x_values.append(x)
            self.y_values.append(y)
            self.step_numbers = len(self.x_values)
            
    def get_step(self):
        direction = choice([1, -1])
        length = choice([1])
        step = direction * length

        return step
      