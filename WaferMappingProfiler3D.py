import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D

database = np.genfromtxt('dataset.csv',delimiter=',')
x = database[1:,0]
y = database[1:,1]
z = database[1:,2]

def plot_contour(x,y,z,resolution = 250,contour_method='linear'):
    resolution = str(resolution)+'j'
    X,Y = np.mgrid[min(x):max(x):complex(resolution), min(y):max(y):complex(resolution)]
    points = [[a,b] for a,b in zip(x,y)]
    Z = griddata(points, z, (X, Y), method=contour_method)
    return X,Y,Z

X,Y,Z = plot_contour(x,y,z, resolution = 250, contour_method='cubic')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z)
plt.show()
# plt.colorbar(orientation = 'vertical', label = 'nm')
# plt.scatter(x,y, color="black", linewidth=0.5, edgecolor="black", s=12)
# plt.axis('off')

# plt.title('Wafer Mapping', loc = 'left')
# for i, txt in enumerate(z):
#     plt.annotate(txt, (x[i], y[i]), size = 12)
#
#
# Info = "Avarage: " + str(np.mean(z)) + '\n' + "Stddev: " + str(np.std(z)) + '\n' + "Range: " + str(np.max(z)-np.min(z))
# plt.text(100,-20, Info, fontsize=12)
#
# plt.savefig('Film Thickness Profile.png')
# plt.show()
