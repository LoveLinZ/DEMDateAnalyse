import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from osgeo import gdal


# ds = gdal.Open(r'ASTGTM2_N34E108_dem.tif')
# data = ds.GetRasterBand(1).ReadAsArray()
# plt.imshow(data, cmap = 'gray')
# plt.show()

ds = gdal.Open(r'ASTGTM2_N34E109_dem.tif')
band = ds.GetRasterBand(1)
# ov_band = band.GetOverview(band.GetOverviewCount() - 3)
# data = ov_band.ReadAsArray()
data = band.ReadAsArray()
# geotransform = ds.GetGeoTransform()
# minx = geotransform[0]
# maxy = geotransform[3]
# maxx = minx + ov_band.XSize * geotransform[1]
# miny = maxy + ov_band.YSize * geotransform[5]
# x = np.arange(minx, maxx, geotransform[1])
# y = np.arange(maxy, miny, geotransform[5])
# x, y = np.meshgrid(x[:ov_band.XSize], y[:ov_band.YSize])
x, y = np.meshgrid(np.arange(band.XSize), np.arange(band.YSize))

fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot_surface(x, y, data, cmap='gist_earth', lw=0)
plt.axis('equal')
plt.show()


