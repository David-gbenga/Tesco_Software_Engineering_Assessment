import heapq

from typing import List, Tuple, Dict

def minim_meeting_room(intervals: List[List[int]])->int:
    #validate input
    if not intervals:
        return 0
    #sort interval with start time
    intervals.sort(key = lambda interval: interval[0])
    
    #create heap to store end time for time intervals to deduce minimum number of rooms 
    heap = [] # stacks up end times with minimum end time occupying heap[0]
    
    #initiate the heap to store end time
    heapq.heappush(heap, intervals[0][1])
    
    #iterate through the other meeting time intervals
    for start, end in intervals[1:]:
        
        #check if the there is an overalap between the minimum heap time and start time
        if heap[0] <= start:
            heapq.heappop(heap) # e.g [9] <= [10] =>True, 9 goes out 
            
        heapq.heappush(heap,end)    # Then [20],the end time for start time 10 takes the place of 9
        
    return len(heap)


if __name__=="__main__":
         intervals = [[0, 30], [5, 10], [15, 20]]
         
         result = minim_meeting_room(intervals)
         
         print(result)