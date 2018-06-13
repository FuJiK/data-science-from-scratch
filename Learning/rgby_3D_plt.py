from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
for c, z in zip(['r', 'g', 'b', 'y'], [60, 40, 20, 0]): # Y���̊Ԋu�𒲐�
    xs = np.arange(20) # �O���t�ׂ̍���
    ys = np.random.rand(20) # �O���t�ׂ̍���
    # You can provide either a single color or an array. To demonstrate this,
    # the first bar of each set is colored cyan.
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()