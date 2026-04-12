# Example
import rasterio
import numpy as np 
from matplotlib import pyplot

def scale(band): # scale values for display purposes. May need adjusting as per your image. 
    return band / 200.0

# Load the blue layer given the folder and filename
my_raster_image = rasterio.open('raw\Montcalm_glacier\01_01_2026\2026-01-06-00_00_2026-01-06-23_59_Sentinel-2_L1C_B02_(Raw).tiff')
blue = scale(my_raster_image.read()[0])

# Load the green layer given the folder and filename
my_raster_image = rasterio.open('raw\Montcalm_glacier\01_01_2026\2026-01-06-00_00_2026-01-06-23_59_Sentinel-2_L1C_B03_(Raw).tiff')
green = scale(my_raster_image.read()[0])

# Load the red layer given the folder and filename
my_raster_image = rasterio.open('raw\Montcalm_glacier\01_01_2026\2026-01-06-00_00_2026-01-06-23_59_Sentinel-2_L1C_B04_(Raw).tiff')
red = scale(my_raster_image.read()[0])

# Load the nir layer given the folder and filename
my_raster_image = rasterio.open('raw\Montcalm_glacier\01_01_2026\2026-01-06-00_00_2026-01-06-23_59_Sentinel-2_L1C_B08_(Raw).tiff')
nir = scale(my_raster_image.read()[0])



# Now we need to stack our layers into a single multi-dimensional numpy array
rgb = np.dstack((red, green, blue))

#
ndvi = (nir - red) / (nir + red)
# Based on McFeeters (1996)
ndwi = (green - nir) / (green + nir)
pyplot.imshow(ndvi)
#my_raster_image.bounds
# print(169.1895-156.2977, "km")
my_raster_image.res
# my_raster_image.crs