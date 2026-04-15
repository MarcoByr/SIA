import cv2 
import rasterio as rio
from skimage.metrics import mean_squared_error,peak_signal_noise_ratio,structural_similarity
import matplotlib.pyplot as plt

# File path
img_path = 'raw\Montcalm_glacier\01_01_2026\2026-01-06-00_00_2026-01-06-23_59_Sentinel-2_L1C_B08_(Raw).tiff'

# Reading the image
image = cv2.imread(img_path)
plt.imshow(image)