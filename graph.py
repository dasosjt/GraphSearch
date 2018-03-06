import numpy as np
from collections import deque
from itertools import islice


class Graph():
  def graph_search(self, problem=None, search_type='BFS'):
    initial_state = [problem.initial_state[0]]
    frontier = deque([initial_state])
    explored = set()

    while True:
      if len(frontier):
        path, frontier = self.remove_choice(frontier, problem, search_type)
        s = path[-1]
        explored.add(s)

        if problem.goal_test(s):
          return path

        for a in problem.actions(s):
          result = problem.result(s, a)
          if result not in explored:
            new_path = []
            new_path.extend(path)
            new_path.append(result)
            frontier.append(new_path)
      else:
        return False

  def remove_choice(self, frontier=None, problem=None, search_type='BFS'):
    if search_type is 'BFS':
      return frontier.popleft(), frontier
    elif search_type is 'DFS':
      return frontier.pop(), frontier
    elif search_type is 'H2':
      results = []
      for path in frontier:
        results.append(problem.heuristic_2(path[-1]))
      (i, value) = min(enumerate(results), key=lambda x: x[1])
      first_part = deque(islice(frontier, 0, i))
      last_part = deque(islice(frontier, i+1, len(frontier)))
      path = list(islice(frontier, i, i+1))[0]
      frontier = deque()
      frontier.extend(first_part)
      frontier.extend(last_part)
      return path, frontier
    elif search_type is 'H1':
      results = []
      for path in frontier:
        results.append(problem.heuristic_1(path[-1]))
      (i, value) = min(enumerate(results), key=lambda x: x[1])
      first_part = deque(islice(frontier, 0, i))
      last_part = deque(islice(frontier, i+1, len(frontier)))
      path = list(islice(frontier, i, i+1))[0]
      frontier = deque()
      frontier.extend(first_part)
      frontier.extend(last_part)
      return path, frontier

