!mamba install rasterio

##------- Import useful libraries -------##

import rasterio
import collections
import numpy as np 
from matplotlib import pyplot

##------- Scaling rasters -------##

def scale(band): # scale values for display purposes. May need adjusting as per your image. 
    return band / 200.0

##------- Loading rasters data -------##

# Load the blue layer given the folder and filename
my_raster_image = rasterio.open('raw_rasters/2025-06-28-00_00_2025-06-28-23_59_Sentinel-2_L2A_B02_(Raw).tif')
blue = scale(my_raster_image.read()[0])

# Load the green layer given the folder and filename
my_raster_image = rasterio.open('raw_rasters/2025-06-28-00_00_2025-06-28-23_59_Sentinel-2_L2A_B03_(Raw).tif')
green = scale(my_raster_image.read()[0])

# Load the red layer given the folder and filename
my_raster_image = rasterio.open('raw_rasters/2025-06-28-00_00_2025-06-28-23_59_Sentinel-2_L2A_B04_(Raw).tif')
red = scale(my_raster_image.read()[0])

# Load the nir layer given the folder and filename
my_raster_image = rasterio.open('raw_rasters/2025-06-28-00_00_2025-06-28-23_59_Sentinel-2_L2A_B08_(Raw).tif')
nir = scale(my_raster_image.read()[0])

##------- Calculate differences index -------##

# Now we need to stack our layers into a single multi-dimensional numpy array
rgb = np.dstack((red, green, blue))
# Normalized Difference Vegetation Index
ndvi = (nir | red) / (nir + red)
# Based on McFeeters (1996)
ndwi = (green | nir) / (green + nir)
type(ndwi)

##------- Print and save images -------##

fig, axs = pyplot.subplots(3, 2,figsize=(15, 15))
fig.tight_layout(pad=0.4, w_pad=0.5, h_pad=3)
axs[0, 0].imshow(red)
axs[0, 0].set_title("RED",fontweight="bold", color="red")
axs[0, 1].imshow(green)
axs[0, 1].set_title("GREEN",fontweight="bold", color="green")
axs[1, 0].imshow(blue)
axs[1, 0].set_title("BLUE",fontweight="bold", color="blue")
axs[1, 1].imshow(nir)
axs[1, 1].set_title("NIR",fontweight="bold")
axs[2, 0].imshow(ndvi)
axs[2, 0].set_title("NDVI",fontweight="bold")
pyplot.imsave('Processed/NDVI.png', ndvi)
axs[2, 1].imshow(ndwi)
axs[2, 1].set_title("NDWI",fontweight="bold")
pyplot.imsave('Processed/NDWI.png', ndwi)

##------- Calculate and save index surface percentage -------##

def classify_ndvi(ndvi):
    classified = np.full(ndvi.shape, -1, dtype='int8') #-1 = no data
    classified[(ndvi >= -1) & (ndvi < 0.2)] = 0  #barren/water
    classified[(ndvi >= 0.2) & (ndvi <= 0.5)] = 1 #moderate vegetation
    classified[(ndvi > 0.5) & (ndvi <= 1)] = 2 #healthy/high vegetation
    return classified
    
def classify_ndwi(ndwi):
    classified = np.full(ndwi.shape, -1, dtype='int8') #-1 = no data
    classified[(ndwi >= -1) & (ndwi < 0.2)] = 0  #barren/water
    classified[(ndwi >= 0.2) & (ndwi <= 0.5)] = 1 #moderate vegetation
    classified[(ndwi > 0.5) & (ndwi <= 1)] = 2 #healthy/high vegetation
    return classified

# appling to ndvi array
classified_ndvi = classify_ndvi(ndvi)

# appling to ndvi array
classified_ndwi = classify_ndwi(ndwi)
classified_ndwi

##------- Calculate and save index stats infos -------##

cv0 = np.count_nonzero(classified_ndvi == 0)
pv0 = c0/classified_ndvi.size*100
cv1 = np.count_nonzero(classified_ndvi == 1)
pv1 = c1/classified_ndvi.size*100
cv2 = np.count_nonzero(classified_ndvi == 2)
pv2 = c2/classified_ndvi.size*100

cw0 = np.count_nonzero(classified_ndwi == 0)
pw0 = cw0/classified_ndwi.size*100
cw1 = np.count_nonzero(classified_ndwi == 1)
pw1 = cw1/classified_ndwi.size*100
cw2 = np.count_nonzero(classified_ndwi == 2)
pw2 = cw2/classified_ndwi.size*100

index_stats=np.array([["Classified Vegetation index statistical infos",cv0,cv1,cv2,pv0,pv1,pv2],["Classified Water index statistical infos",cw0,cw1,cw2,pw0,pw1,pw2]])

bold = "\033[1m"
reset = "\033[0m"

print(f'\n{bold}{'Vegetation Index infos'}{reset}')
print('----------------')
print('NDVI values  Min : %s | Max : %s | Mean : %s | Med : %s' % (np.min(ndvi),np.max(ndvi),round(np.mean(ndvi),5),round(np.median(ndvi),5)))
print('Classified NDVI values  Min : %s | Max : %s | Mean : %s' % (np.min(classified_ndvi),np.max(classified_ndvi),round(np.mean(classified_ndvi),5)))
print('Occurence Vegetation index  0 : %s | 1 : %s | 2 : %s' % (cv0,cv1,cv2))
# print('Percentage Vegetation index -> 0 : %s %% - 1 : %s %% - 2 : %s %%' % (round(p0,2),round(p1,2),round(p2,2)))
print(f'Percentage Vegetation index -> 0 : {bold}{round(pv0,2)}{"%"}{reset} | 1 : {bold}{round(pv1,2)}{"%"}{reset} | 2 : {bold}{round(pv2,2)}{"%"}{reset}')

print(f'\n{bold}{'Water Index infos'}{reset}')
print('----------------')
print('NDWI values  Min : %s | Max : %s | Mean : %s | Med : %s' % (np.min(ndwi),np.max(ndwi),round(np.mean(ndwi),5),round(np.median(ndwi),5)))
print('Classified NDWI values  Min : %s | Max : %s | Mean : %s' % (np.min(classified_ndwi),np.max(classified_ndwi),round(np.mean(classified_ndwi),5)))
print('Occurence Water index  0 : %s | 1 : %s | 2 : %s' % (cw0,cw1,cw2))
print(f'Percentage Water index -> 0 : {bold}{round(pw0,2)}{"%"}{reset} | 1 : {bold}{round(pw1,2)}{"%"}{reset} | 2 : {bold}{round(pw2,2)}{"%"}{reset}')

# print(classified_ndvi)
np.savetxt('Processed/Classified_NDVI.txt', classified_ndvi, delimiter=';',newline='\n',  header='##----- Classified NDVI array -----## \n', comments='## Export the Classified NDVI indexes to postcalculate the surface percentage of vegetation ##')
np.savetxt('Processed/NDVI.txt', ndvi, delimiter=';',newline='\n',  header='##----- NDVI_array -----## \n', comments='## Export the NDVI array to postcalculate the surface percentage of vegetation ##')
# np.savetxt('Processed/Index_stats_infos.txt', index_stats, delimiter=';',newline='\n',  header='##----- Index statisticals datas -----## \n', comments='## Export the differents index (water, vegatation, and more if desired) statistical informations ##')
with open('Processed/Index_stats_infos.txt','w') as f:
     f.write('\n'.join([str(item) for sublist in index_stats for item in sublist]))



