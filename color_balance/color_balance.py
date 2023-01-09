import numpy as np
from matplotlib.patches import Rectangle
from skimage.io import imread, imshow
from matplotlib import pyplot as plt
import skimage.io as skio
import cv2
from skimage import img_as_ubyte, img_as_float


overcast  = imread("lenna.png");
plt.figure(num=None, figsize = (8,5),dpi = 80);
imshow(overcast);


fig, ax = plt.subplots(1,1, figsize=(8, 6), dpi = 80)
patch = Rectangle((70,175), 10, 10, edgecolor='r', facecolor='none')
ax.add_patch(patch)
ax.imshow(overcast);

coord = Rectangle.get_bbox(patch).get_points()
print(coord)

fig, ax = plt.subplots(1,1, figsize=(8, 6), dpi = 80)
ax.imshow(overcast[int(coord[0][1]):int(coord[1][1]),
                   int(coord[0][0]):int(coord[1][0])]);


image_patch = overcast[int(coord[0][1]):int(coord[1][1]),
                       int(coord[0][0]):int(coord[1][0])]
image_max = (overcast / image_patch.max(axis=(0, 1))).clip(0, 1)
image_mean = ((overcast * image_patch.mean())
               / overcast.mean(axis=(0, 1))).clip(0,255).astype(int)
fig, ax = plt.subplots(1,2, figsize=(15, 10), dpi = 80)
f_size = 19
ax[0].imshow(image_max)
ax[0].set_title('Max Adjusted', fontsize = f_size)
ax[0].set_axis_off()
ax[1].set_title('Mean Adjusted', fontsize = f_size)
ax[1].imshow(image_mean);
ax[1].set_axis_off()
fig.tight_layout()
