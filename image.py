import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

class Image():
  def __init__(self, name, N):
    self.N = N
    self.l = misc.imread(name)
    (self.H, self.W, _) = self.l.shape
    self.discrete_image = np.zeros(shape=(np.floor(self.H/self.N).astype(np.int64), np.floor(self.W/self.N).astype(np.int64), 3))

  def rgb_median(self, rgb_matrix):
    median = np.median(rgb_matrix, axis=(0, 1))
    if median[2] > 110 and median[1] > 110 and median[0] > 110:
      return np.array([255,255,255])
    elif median[1] > 120:
      return np.array([0, 255, 0])
    elif median[0] > 128:
      return np.array([255, 0, 0])
    else:
      return np.array([0, 0, 0])
    #return self.diff_color(median)

  def diff_color(self, median):
    red = abs(median[0] - median[1]) + abs(median[0] - median[2])
    blue = abs(median[1] - median[0]) + abs(median[1] - median[2])
    green = abs(median[2] - median[1]) + abs(median[2] - median[0])

    if (max(red, blue, green) < 20 and median[0] > 100):
      # This is white
      return np.array([255,255,255])
    elif (red > blue and red > green):
      # This is red
      return np.array([255, 0, 0])
    elif (blue > red and blue > green):
      # This is blue
      return np.array([255, 255, 255])
    elif (green > red and green > blue):
      return np.array([0, 255, 0])
    else:
      return np.array([0, 0, 0])

  def apply_discrete(self):
    for y in range(0, np.floor(self.H/self.N).astype(np.int64)):
      for x in range(0, np.floor(self.W/self.N).astype(np.int64)):
        self.discrete_image[y][x] = self.rgb_median(self.l[y*self.N:(y+1)*self.N, x*self.N:(x+1)*self.N])

  def apply_result(self, result):
    for p in result:
      (y, x) = p
  
      if np.array_equal(self.discrete_image[y][x], np.array([255, 255, 255])):
        self.discrete_image[y][x] = np.array([24, 0, 111])

  def show_uint8(self):
    plt.imshow(np.uint8(self.discrete_image))
    plt.show()