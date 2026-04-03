# Example
import rasterio
import numpy as np 
from matplotlib import pyplot

def scale(band): # scale values for display purposes. May need adjusting as per your image. 
    return band / 200.0

# Load the blue layer given the folder and filename
my_raster_image = rasterio.open('2025-06-28-00_00_2025-06-28-23_59_Sentinel-2_L2A_B02_(Raw).tiff')
blue = scale(my_raster_image.read()[0])

# Load the green layer given the folder and filename
my_raster_image = rasterio.open('2025-06-28-00_00_2025-06-28-23_59_Sentinel-2_L2A_B03_(Raw).tiff')
green = scale(my_raster_image.read()[0])

# Load the red layer given the folder and filename
my_raster_image = rasterio.open('2025-06-28-00_00_2025-06-28-23_59_Sentinel-2_L2A_B04_(Raw).tiff')
red = scale(my_raster_image.read()[0])

# Load the nir layer given the folder and filename
my_raster_image = rasterio.open('2025-06-28-00_00_2025-06-28-23_59_Sentinel-2_L2A_B08_(Raw).tiff')
nir = scale(my_raster_image.read()[0])

# Now we need to stack our layers into a single multi-dimensional numpy array
rgb = np.dstack((red, green, blue))

#
ndvi = (nir - red) / (nir + red)
# Based on McFeeters (1996)
ndwi = (green - nir) / (green + nir)
pyplot.imshow(ndvi, ndwi)