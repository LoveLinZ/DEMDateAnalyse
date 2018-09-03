import os
import numpy as np
from osgeo import gdal
import ospybook as pb

in_fn = r'Near1000M.tif'
out_fn = r'Near1000MSmooth.tif'
in_ds = gdal.Open(in_fn)
in_band = in_ds.GetRasterBand(1)
in_data = in_band.ReadAsArray()
slices = pb.make_slices(in_data, (3, 3))
stacked_data = np.ma.dstack(slices)

rows, cols = in_band.YSize, in_band.XSize
out_data = np.ones((rows, cols), np.int32) * -99
out_data[1:-1, 1:-1] = np.mean(stacked_data, 2)

pb.make_raster(in_ds, out_fn, out_data, gdal.GDT_Int32, -99)
