import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from osgeo import gdal
import matplotlib.animation as animation
from matplotlib.colors import LightSource

# ds = gdal.Open(r'Near3000MSmooth.tif')
# data = ds.GetRasterBand(1).ReadAsArray()
# plt.imshow(data)
# plt.show()

ds = gdal.Open(r'Near1000MSmooth.tif')
band = ds.GetRasterBand(1)
# ov_band = band.GetOverview(band.GetOverviewCount() - 3)
# data = ov_band.ReadAsArray()
data = band.ReadAsArray()
# geotransform = ds.GetGeoTransform()
# minx = geotransform[0]
# maxy = geotransform[3]
# maxx = minx + band.XSize * geotransform[1]
# miny = maxy + band.YSize * geotransform[5]
# x = np.arange(minx, maxx, geotransform[1])
# y = np.arange(maxy, miny, geotransform[5])
# x, y = np.meshgrid(x[:band.XSize], y[:band.YSize])
x, y = np.meshgrid(np.arange(band.XSize), np.arange(band.YSize))
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot_surface(x, y, data, cmap = 'gist_earth', lw = 0)
plt.axis('equal')

# ax.view_init(elev = 55, azim = 60)
# plt.axis('off')
# def animate(i):
#     ax.view_init(elev = 65,azim = i)
# anim = animation.FuncAnimation(fig, animate, frames = range(0, 360, 10), interval = 100)
plt.show()


