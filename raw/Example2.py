import cv2 
from skimage.metrics import mean_squared_error,peak_signal_noise_ratio,structural_similarity
import matplotlib.pyplot as plt

# File path
img_path = '2025-06-28-00_00_2025-06-28-23_59_Sentinel-2_L2A_True_color..tiff'

# Reading the image
image = cv2.imread(img_path)
image
