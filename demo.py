# load pcd

# packages
from PIL import Image
#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

image_data = Image.open('000000.png')
plt.imshow(image_data)

lidar_file = open('000000.bin', 'rb')
lidar_raw = np.fromfile(lidar_file, dtype=np.float32, count=-1) # 1-D array: (461536L,)
lidar_file.close()
lidar_data = lidar_raw.reshape(int(len(lidar_raw)/4), 4) # 2-D array: (115384L, 4L)


# plot pcd
X = lidar_data[:, 0]
Y = lidar_data[:, 1]
Z = lidar_data[:, 3]

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect('equal')

scat = ax.scatter(X, Y, Z)

# Create cubic bounding box to simulate equal aspect ratio
max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max()
Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(X.max()+X.min())
Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(Y.max()+Y.min())
Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(Z.max()+Z.min())
# Comment or uncomment following both lines to test the fake bounding box:
for xb, yb, zb in zip(Xb, Yb, Zb):
   ax.plot([xb], [yb], [zb], 'w')

plt.grid()
plt.show()


























#print (lidar_data.shape) # (115384L, 4L)
#print (type(lidar_data)) # numpy.ndarray
#print (lidar_data)

#image_data = Image.open('000000.png')
##plt.imshow(image_data)
#
#
##fig = plt.figure(1, figsize=(10, 6))
##ax = fig.add_subplot(111, projection='3d')
#ax.scatter(lidar_data[:, 0], lidar_data[:, 1], lidar_data[:, 3], s=1)
#ax.set_xlabel('X Label'), ax.set_ylabel('Y Label'), ax.set_zlabel('Z Label')
##plt.axis('equal')
#
#
#plt.gca().set_aspect('equal', adjustable='box')
#plt.draw()
##plt.show()
#
##fig = plt.figure()
##ax = fig.gca(projection='3d')
##ax.set_aspect('equal')
##
##
##X = lidar_data[:, 0]
##Y = lidar_data[:, 1]
##Z = lidar_data[:, 3]
##
##scat = ax.scatter(X, Y, Z)
##
##max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0
##
##mid_x = (X.max()+X.min()) * 0.5
##mid_y = (Y.max()+Y.min()) * 0.5
##mid_z = (Z.max()+Z.min()) * 0.5
##ax.set_xlim(mid_x - max_range, mid_x + max_range)
#ax.set_ylim(mid_y - max_range, mid_y + max_range)
#ax.set_zlim(mid_z - max_range, mid_z + max_range)
#
#plt.show()


