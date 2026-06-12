"""Question : COUNT ELEMENT GREATER PREVIOUS AVERAGE
Given an array of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.
Example
Input
responseTimes = [100, 200, 150,300]
Output
2
"""

def countResponseTimeRegressions(responseTimes):
        
        n  = len(responseTimes)
        if n <= 1:
                return 0
        count = 0
        runn_sum = responseTimes[0]
        for i in range(1,n):
                if responseTimes[i] > runn_sum/i:
                        count += 1
                runn_sum += responseTimes[i]
        return count                
                
                
                
        
if __name__=="__main__":
        response_time = [20,50,60,35,75]
        
        result = countResponseTimeRegressions(response_time)
        
        print(result) 
        