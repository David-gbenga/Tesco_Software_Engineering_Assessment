"""
Top K Frequent Events with Order Preservation
Given an array of integers and an integer k, return an array of the k most frequent elements. If two elements have the same frequency, prioritize the one that appears first.

Example 1

Input:

events = [1, 2, 1, 3, 2, 1]
k = 2
Output:

[1, 2]
"""

from typing import List, Tuple, Dict

def top_k_frequent_events(events: List[int], k:int)-> List[int]:
    
    #Validate all inputs and set values for exceptions 
    if not isinstance(events, list):
        raise TypeError("events must be a list of integers")
    
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    if k <0 :
        raise ValueError("k must eaither be zero or greater than zero")
    
    if k==0 or not events:
        return []
    
    #create dictionaries to for event frequencies and event index
    
    frequency = {}
    
    first_appearance = {}
    
    #loop through events to create populate the above dictionaries
    
    for index, event in enumerate(events):
        
        if not isinstance(event, int):
            raise TypeError( "event must be in integer format")
        
        if event not in first_appearance:
            first_appearance[event] = index
            
        frequency[event] = frequency.get(event,0) + 1
        
        
    # create a list that sort each events with respect to the highest occurrence and first appearance event index     
    
    sorted_list : List[int] = sorted(frequency.keys(),
     key= lambda event: (-frequency[event], first_appearance[event]) )    
    
    #return final list using k S LIMIT FOR OUTPUT
    
    return sorted_list[:k]



if __name__ == "__main__":
    
    events = [1, 2, 1, 3, 2, 1]
    k = 2
    
    result = top_k_frequent_events(events,k)
    
    print(result)
    