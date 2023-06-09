# Prompt
# Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix
# The input of the function should be a list containing 9 digits
# The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix
# The returned dictionary should follow this format:
# {
#  'mean': [axis1, axis2, flattened],
#  'variance': [axis1, axis2, flattened],
#  'standard deviation': [axis1, axis2, flattened],
#  'max': [axis1, axis2, flattened],
#  'min': [axis1, axis2, flattened],
#  'sum': [axis1, axis2, flattened]
# }
# If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers."
# The values in the returned dictionary should be lists and not Numpy arrays

import numpy as np

def calculate(mylist):
  
  # create a list and raise a value error if not equal to 9

  if len(mylist) != 9:
    raise ValueError ('List must contain nine numbers.')

  # create an array and reshape it to a 3 by 3 matrix
  # create an empty dictionary
  
  ls = np.array(mylist)
  mat = ls.reshape((3,3))
  calculations = dict()

  # assign key value pairs to the calculations dictionary
  # calculate values asked for (mean, var, std, max, min, sum) for each axis of the matrix plus the flattened list
  # use list() to convert the np array to a python list
  
  calculations['mean'] = [list(np.mean(mat, axis=0)), list(np.mean(mat, axis=1)), np.mean(ls)]
  calculations['variance'] = [list(np.var(mat, axis=0)), list(np.var(mat, axis=1)), np.var(ls)]
  calculations['standard deviation'] = [list(np.std(mat, axis=0)), list(np.std(mat, axis=1)), np.std(ls)]
  calculations['max'] = [list(np.max(mat, axis=0)), list(np.max(mat, axis=1)), np.max(ls)]
  calculations['min'] = [list(np.min(mat, axis=0)), list(np.min(mat, axis=1)), np.min(ls)]
  calculations['sum'] = [list(np.sum(mat, axis=0)), list(np.sum(mat, axis=1)), np.sum(ls)]

  # return all values from the calculations dictionary
  
  return calculations
