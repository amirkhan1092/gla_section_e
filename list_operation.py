#
# def prime(i):
#     for k in range(2,i):
#         if i%k==0:
#             return False
#     else:
#         return True
#
# a=[2,4,5,6,7,8,9,55,87]
#
# print(a)
#
# h=list(filter(prime,a))
# print(h)


# Python version
import sys

print('Python: {}'.format(sys.version))
# scipy
import scipy

print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy

print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib

print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas

print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn

print('sklearn: {}'.format(sklearn.__version__))

