import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from osgeo import gdal
import matplotlib.animation as animation

# ds = gdal.Open(r'MergeDemData.tif')
# data = ds.GetRasterBand(1).ReadAsArray()
# plt.imshow(data)
# plt.show()

ds = gdal.Open(r'Near1000MbilinearSmooth.tif')
band = ds.GetRasterBand(1)
data = band.ReadAsArray()
x, y = np.meshgrid(np.arange(band.XSize), np.arange(band.YSize))

max_range = np.array([2000 * (x.max()-x.min()), 2000 * (y.max()-y.min()), data.max()-data.min()]).max()/2
mid_x = (2000 * (x.max()-x.min()))/2
mid_y = (2000 * (y.max()-y.min()))/2
mid_z = (data.max()-data.min())/2
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect('equal')
ax.plot_surface(x*2000, y*2000, data*1.5, cmap='gist_earth', lw=0)
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)
# plt.axis('equal')
# ax.view_init(elev = 55, azim = 60)
# plt.axis('off')
# def animate(i):
#     ax.view_init(elev = 65,azim = i)
# anim = animation.FuncAnimation(fig, animate, frames = range(0, 360, 10), interval = 100)
plt.show()


