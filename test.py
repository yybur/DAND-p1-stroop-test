import csv
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')


con = [12.079, 16.791, 9.564, 8.63, 14.669, 12.238, 14.692, 8.987, 9.401, 14.48, 22.328, 15.298, 15.073, 16.929, 18.2, 12.13, 18.495, 10.639, 11.344, 12.369, 12.944, 14.233, 19.71, 16.004]
incon = [19.278, 18.741, 21.214, 15.687, 22.803, 20.878, 24.572, 17.394, 20.762, 26.282, 24.524, 18.644, 17.51, 20.33, 35.255, 22.158, 25.139, 20.429, 17.425, 34.288, 23.894, 17.96, 22.058, 21.157]
data = np.vstack([con, incon]).T
bins = np.linspace(0, 30, 10)

plt.hist(data, bins, alpha=0.7, label=['congruent', 'incongruent'])
plt.legend(loc='upper right')
plt.show()
