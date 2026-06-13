"""
Find the Smallest Missing Positive Integer
Given an unsorted array of integers, find the smallest positive integer not present in the array in O(n) time and O(1) extra space.

Example

Input

orderNumbers = [3, 4, -1, 1]
Output

2



"""
def findSmallestMissingPositive(orderNumbers):
    order_set = set(x for x in orderNumbers if x>0)
    
    missing = 1
    
    while missing in order_set:
        missing +=1
    return missing    
    
    
    