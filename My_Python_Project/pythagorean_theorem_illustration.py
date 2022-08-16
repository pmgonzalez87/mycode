from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt

vertices = []
codes = []

codes += [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]
vertices += [(2, 2.5), (3.5, 4), (3.5, 2.5), (0, 0)]

path = Path(vertices, codes)

pathpatch = PathPatch(path, facecolor='none', edgecolor='blue')

fig, ax = plt.subplots()
ax.add_patch(pathpatch)
ax.set_title('Pythagorean Theorem Formualas')

ax.autoscale_view()

plt.show()
