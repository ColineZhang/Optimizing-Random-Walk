from RandomWalk import RandomWalk
from AlteredWalk import AlteredWalk

#from AlteredWalk import AlteredWalk

class Generation:

  def __init__(self, population=10):
    self.paths = []
    self.population = population
    self.generate()
    self.optimum = {'step_numbers':self.paths[0]['step_numbers']}
    self.optimize()

  def generate(self):
    
    for i in range(0,self.population):
      rw = RandomWalk()
      path_info = {}
      path_info['x_values'] = rw.x_values
      path_info['y_values'] = rw.y_values
      path_info['step_numbers'] = rw.step_numbers
      self.paths.append(path_info)

  def optimize(self):

    for i in self.paths:
      if i['step_numbers'] < self.optimum['step_numbers']:
        self.optimum['step_numbers'] = i['step_numbers']
        self.optimum['x_values'] = i['x_values']
        self.optimum['y_values'] = i['y_values']
        
class SpecGeneration():
  def __init__(self, parent_path, population=10):
    self.parent_path = parent_path
    #print(parent_path.keys())
    self.paths = []
    self.population = population
    self.generate()
    
    self.optimum = {'step_numbers':self.paths[0]['step_numbers'], 'x_values':self.paths[0]['x_values'], 'y_values':self.paths[0]['y_values']}
    self.optimize()
  def generate(self):
    aw = AlteredWalk(self.parent_path['x_values'], self.parent_path['y_values'], self.parent_path['step_numbers'])
    path_info = {}
    path_info['x_values'] = aw.x_values
    path_info['y_values'] = aw.y_values
    path_info['step_numbers'] = aw.step_numbers           
    self.paths.append(path_info)
  def optimize(self):
    for i in self.paths:
      if i['step_numbers'] < self.optimum['step_numbers']:
        self.optimum['step_numbers'] = i['step_numbers']
        self.optimum['x_values'] = i['x_values']
        self.optimum['y_values'] = i['y_values']
      