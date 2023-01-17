import matplotlib.pyplot as plt
from Generation import Generation
from Generation import SpecGeneration
gn = Generation()
for i in range(1,11):
  print(f"The shortest path length in generation {i} is {gn.optimum['step_numbers']}")
  optimum = gn.optimum
  gn = SpecGeneration(optimum)
def display(x_values, y_values, step_numbers, color='green'):
    plt.style.use('classic')

    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, color=color, linewidth=1)

    ax.set_title(f'Random Walk {step_numbers}', fontsize=20)
    plt.show()
'''test = sg.optimum
display(test['x_values'],test['y_values'],test['step_numbers'])'''

'''display(rw.x_values, rw.y_values, rw.step_numbers, 'green')
time.sleep(5.0)
print('new')
display(aw.x_values, aw.y_values, aw.step_numbers, 'red')
'''

'''plt.plot(rw.x_values, rw.y_values, label = "line 1", linewidth=3)
plt.plot(aw.x_values, aw.y_values, label = "line 2", linewidth=1)
plt.show()'''