#Given an array of integers, return the highest product possible by multiplying 3 numbers from the array
#
#Input:
#
#array of integers e.g {1, 2, 3}
# NOTE: Solution will fit in a 32-bit signed integer 
#Example:
#
#[0, -1, 3, 100, 70, 50]
#
#=> 70*50*100 = 350000
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A_sorted = sorted(A)
        if A_sorted[-1] < 0:
            return A_sorted[-1] * A_sorted[-2] * A_sorted[-3]
        elif A_sorted[-1] == 0:
            return 0
        elif A_sorted[-2] <0 or A_sorted[-3] <0:
            return A_sorted[0] * A_sorted[1] * A_sorted[-1]
        else:
            return max(A_sorted[0] * A_sorted[1] * A_sorted[-1], A_sorted[-1]*A_sorted[-2]*A_sorted[-3])
