"""
Build a simple model registry selector
Question:
Given multiple trained model records, return the best deployable model based on highest metric and status "approved".
Input:
models = [ {"version": "v1", "auc": 0.81, "status": "approved"}, {"version": "v2", "auc": 0.84, "status": "failed"}, {"version": "v3", "auc": 0.83, "status": "approved"} ]
Output:
{"version": "v3", "auc": 0.83, "status": "approved"} Test focus: filtering, tie-breaking, no approved model.

"""

from typing import List, Dict




def model_selector(models: List[Dict])->Dict:
    
    """
    this selects the hightes metric model that is approved
    
    arg:
    models
    
    return:
    model
    """
    
    # input validation
    if not isinstance(models, list):
        raise TypeError("models must be a list")
    
    if not models:
        return {}
    
    for model in models:
        if not isinstance(model, dict):
            raise TypeError("model must be a dictionary")
        if not model:
            return {}
    
    
    #list to safe approved models 
    approved_models = []
    
    #loop throgh to get approvced models ....
              
    approved_models = [ model for model in models if model.get("status")=="approved"]
                    
    
    #rank model with highest metric
    ranked_model = max(approved_models, key = lambda model:model["auc"]  )   
                
    return ranked_model      
    
    
    
    
if __name__ == "__main__":
    
    models = [ {"version": "v1", "auc": 0.81, "status": "approved"}, {"version": "v2", "auc": 0.84, "status": "failed"}, {"version": "v3", "auc": 0.83, "status": "approved"} ]
    
    result = model_selector(models)
    
    print(result)


        