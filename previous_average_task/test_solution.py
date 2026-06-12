from solution import countResponseTimeRegressions

def test_ideal_values():
    responseTimes =  [100, 200, 150, 300]
    assert countResponseTimeRegressions(responseTimes)==2
    
    
def test_empty_array():
    responseTimes =  []
    assert countResponseTimeRegressions(responseTimes) == 0
    
    
def test_one_value():
    responseTimes = [100]
    assert countResponseTimeRegressions(responseTimes) == 0
    
def test_all_values_increasing():
    responseTimes = [100,200,300,400,500]
    assert countResponseTimeRegressions(responseTimes) == 4
    
def test_all_values_same():
    responseTimes = [100,100,100,100,100]
    assert countResponseTimeRegressions(responseTimes) == 0    
    
    
def test_all_values_decreasing():
    responseTimes = [100,90,80,70,60]
    assert countResponseTimeRegressions(responseTimes) == 0    
    