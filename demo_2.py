# load and display image and point cloud data

# packages
import numpy as np
import cv2
import mayavi.mlab

img = cv2.imread('000000.png')
cv2.imshow('image',img)

pcd = np.fromfile('000000.bin', dtype=np.float32).reshape((-1, 4)) # reading binary data (and reshape)
mayavi.mlab.points3d(pcd[:, 0], pcd[:, 1], pcd[:, 2], pcd[:, 2], mode="point") # (x, y, z, color, mode)
mayavi.mlab.show()

