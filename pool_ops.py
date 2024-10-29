# pool_ops.py

# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p
# Description: Outputs the shape and operation count of a convolution layer

# Parameters:
#c_in: input channel 
#h_in: input height 
#w_in: input width 
#h_pool: average pooling kernel height 
#w_pool: average pooling kernel width 
#s: stride of average pooling kernel
#p: amount of padding on each of the four input map sides

# Output:
#  Shape and operation count of an average pooling layer

# Written by Maxwell Oross
# Other contributors: None

# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math
import sys


# initialize script arguments
c_in = float(sys.argv[1])
h_in = float(sys.argv[2])
w_in = float(sys.argv[3])
h_pool = float(sys.argv[4])
w_pool = float(sys.argv[5])
s = float(sys.argv[6])
p = float(sys.argv[7])

# parse script arguments
if len(sys.argv)==8:
  c_in = float(sys.argv[1])
  h_in = float(sys.argv[2])
  w_in = float(sys.argv[3])
  h_pool = float(sys.argv[4])
  w_pool = float(sys.argv[5])
  s = float(sys.argv[6])
  p = float(sys.argv[7])
else:
  print(\
   'Usage: '\
   'python3 pool_ops.py c_in h_in w_in h_pool w_pool s p'\
  )
  exit()

h_out = ((h_in + 2*p - h_pool)/s) + 1
w_out = ((w_in + 2*p - w_pool)/s) + 1
c_out = c_in
adds = c_in * h_out * w_out * (h_pool * w_pool -1) 
muls = 0
divs = c_in * h_out * w_out

# Display final answers
print(int(c_out)) # output channel 
print(int(h_out)) # output height 
print(int(w_out)) # output width 
print(int(adds))  # number of additions 
print(int(muls))  # number of multiplications 
print(int(divs))  # number of divisions 


