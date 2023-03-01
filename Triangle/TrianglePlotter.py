import matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


print("By default, one vertex point will be placed at (0,0)")
print("Where would you like your first Vertex to be placed?")
a = int(input("Input your 'a' value: "))
b = int(input("Input your 'b' value: "))
print("Where would you like your second Vertex to be placed?")
c = int(input("Input your 'c' value: "))
d = int(input("Input your 'd' value: "))


def _max(kwargs):
    return max(kwargs) + 1


pts = np.array([[0, 0], [a, b], [c, d]])
p = Polygon(pts, closed=True, color='limegreen')
plt.title('Your Triangle', loc='left')
ax = plt.gca()

ax.add_patch(p)

# sets max x and y window
ax.set_xlim(min(0, a, c) - 1, max(0, a, c) + 1)
ax.set_ylim(min(0, b, d) - 1, max(0, b, d) + 1)

p.set_edgecolor('red')
p.set_linewidth(1.5)
plt.grid()

plt.show()
