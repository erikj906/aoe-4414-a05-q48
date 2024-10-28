# pool_ops.py
#
# Usage: python3 script_name.py arg1 arg2 ...
# Text explaining script usage
# Parameters:
# arg1: description of argument 1
# arg2: description of argument 2
# ...
# Output:
# A description of the script output
#
# Written by Erik Judy
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.
# import Python modules
# e.g., import math # math module
import sys
import math
# "constants"
# helper functions
## function description
# def calc_something(param1, param2):
# pass
# initialize script arguments
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
# write script below this line
h_out = math.floor((h_in + 2*p - h_pool)/s + 1)
w_out = math.floor((w_in + 2*p - w_pool)/s + 1)
c_out = c_in
adds = h_out*w_out*c_in*(h_pool*w_pool - 1)
muls = 0
divs = c_in*h_out*w_out

print(int(c_out))
print(int(h_out))
print(int(w_out))
print(int(adds))
print(int(muls))
print(int(divs)) 