import numpy as np
data = np.array([[3,2],
                [5,8]])

cov_matrix = np.cov(data, rowvar=False)
print('Covariance Matrix')
print(cov_matrix)

mat_m = np.array([[1, 0, 1],
                  [0, 1, 0],
                  [1, 1, 1]])

det_m = np.linalg.det(mat_m)
print('det_m', det_m)