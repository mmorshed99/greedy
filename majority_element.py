#Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.
#
#You may assume that the array is non-empty and the majority element always exist in the array.
#
#Example :
#
#Input : [2, 1, 2]
#Return  : 2 which occurs 2 times which is greater than 3/2. 
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        temp = A[0]
        count = 1
        for i in range(1,len(A)):
            if A[i] == temp:
                count += 1
            else:
                count -= 1
                if count ==0:
                  temp = A[i]
                  count = 1
        return temp
##better one##
def majorityElement(self, A):
        if len(A) == 1:
            return A[0]
        elem_count = {}
        elem_count[A[0]] = 1
        for idx in range(1,len(A)):
            if elem_count.get(A[idx]):
                elem_count[A[idx]] += 1
            else:
                if len(elem_count) == 0:
                    elem_count[A[idx]] = 1
                    continue
                for each_key in elem_count.keys():
                    elem_count[each_key] -= 1
                    if elem_count[each_key] == 0:
                        del elem_count[each_key]
        for each_key in elem_count.keys():
            return each_key
