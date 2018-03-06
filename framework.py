import numpy as np

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

class Problem():
  def __init__(self, matrix):
    self.matrix = matrix
    (self.h, self.w, _) = self.matrix.shape
    print(self.h, self.w)
    self.initial_state = []
    self.goal_state = []
    for iy, y in enumerate(matrix):
      for ix, x in enumerate(y):
        if x[0] == 255 and x[1] == 0 and x[2] == 0:
          self.initial_state.append((iy, ix))
        elif x[0] == 0 and x[1] == 255 and x[2] == 0:
          self.goal_state.append((iy, ix))

    print('Initial state', self.initial_state)
    print('Goal state', self.goal_state)

  def goal_test(self, s):
    return s in self.goal_state

  def actions(self, s):
    actions_list = []
    (y, x) = s

    if y + 1 < self.h and not np.array_equal(self.matrix[y+1, x], np.array([0, 0, 0])):
      actions_list.append(UP)

    if y > 0 and not np.array_equal(self.matrix[y-1, x], np.array([0, 0, 0])):
      actions_list.append(DOWN)

    if x + 1 < self.w and not np.array_equal(self.matrix[y, x+1], np.array([0, 0, 0])):
      actions_list.append(RIGHT)

    if x > 0 and not np.array_equal(self.matrix[y, x-1], np.array([0, 0, 0])):
      actions_list.append(LEFT)

    return actions_list

  def result(self, s, a):
    (y, x) = s

    if a is UP:
      return (y+1, x)
    elif a is DOWN:
      return (y-1, x)
    elif a is RIGHT:
      return (y, x+1)
    else:
      return (y, x-1)

  def path_cost(self, path):
    return len(path)-1

  def heuristic_1(self, s):
    (y, x) = s
    results = []

    for goal in self.goal_state:
      (gy, gx) = goal
      results.append(np.absolute((gy - y) + (gx - x)))
    
    return min(results)

  def heuristic_2(self, s):
    (y, x) = s
    results = []

    for goal in self.goal_state:
      (gy, gx) = goal
      results.append(np.sqrt(np.power(y-gy, 2) + np.power(x-gx, 2)))

    return min(results)