from framework import Problem
from image import Image
from graph import Graph

image = Image('4.bmp', 20)
image.apply_discrete()
image.show_uint8()
problem = Problem(image.discrete_image)
g = Graph()

result = g.graph_search(problem, 'BFS')
if result:
  image.apply_result(result)
else:
  print('No solution found')

image.show_uint8()