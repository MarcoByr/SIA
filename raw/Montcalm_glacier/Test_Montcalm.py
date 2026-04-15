# Example
import rasterio
import numpy as np 
from matplotlib import pyplot

def scale(band): # scale values for display purposes. May need adjusting as per your image. 
    return band / 200.0

#------- Data importation --------#

# Load the blue layer given the folder and filename
my_raster_image = rasterio.open('2026-01-06-00_00_2026-01-06-23_59_Sentinel-2_L1C_B02_(Raw).tiff')
blue = scale(my_raster_image.read()[0])

# Load the green layer given the folder and filename
my_raster_image = rasterio.open('2026-01-06-00_00_2026-01-06-23_59_Sentinel-2_L1C_B03_(Raw).tiff')
green = scale(my_raster_image.read()[0])

# Load the red layer given the folder and filename
my_raster_image = rasterio.open('01_01_2025\2025-01-01-00_00_2025-01-01-23_59_Sentinel-2_L1C_B04_(Raw).tiff"',dtype="uint16")
red = scale(my_raster_image.read()[0])

# Load the nir layer given the folder and filename
my_raster_image = rasterio.open('2026-01-06-00_00_2026-01-06-23_59_Sentinel-2_L1C_B08_(Raw).tiff')
nir = scale(my_raster_image.read()[0])

# Load the nir layer given the folder and filename
my_raster_image = rasterio.open('2026-01-06-00_00_2026-01-06-23_59_Sentinel-2_L1C_True_color.tiff')
TC = scale(my_raster_image.read()[0])

# Load the nir layer given the folder and filename
my_raster_image = rasterio.open('2026-01-06-00_00_2026-01-06-23_59_Sentinel-2_L1C_B11_(Raw).tiff')
swir = scale(my_raster_image.read()[0]) #Short Wave InfraRed

#------- Raster stacking --------#
# Now we need to stack our layers into a single multi-dimensional numpy array
rgb = np.dstack((red, green, blue))

# Normalized Difference Vegetation IndexError()
ndsi = (green - swir) / (green + swir)

# Normalized Difference Vegetation IndexError()
ndvi = (nir - red) / (nir + red)

# Based on McFeeters (1996)
ndwi = (green - nir) / (green + nir)


#------- Image and info printing --------#

pyplot.imshow(red)

#my_raster_image.bounds
my_raster_image.res
# my_raster_image.crs