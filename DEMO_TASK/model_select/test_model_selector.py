import pytest


from model_selector import model_selector



# normal case when all outputs are valid

def test_model_selector_all_inputs_valid():
    models = [ {"version": "v1", "auc": 0.81, "status": "approved"}, {"version": "v2", "auc": 0.84, "status": "failed"}, {"version": "v3", "auc": 0.83, "status": "approved"} ]
    
    assert model_selector(models)=={'version': 'v3', 'auc': 0.83, 'status': 'approved'}
    
    
# test invalid inputs 
# starting with models 

def test_when_model_input_type_invalid():
    models = ( {"version": "v1", "auc": 0.81, "status": "approved"}, {"version": "v2", "auc": 0.84, "status": "failed"}, {"version": "v3", "auc": 0.83, "status": "approved"} )
    
    with pytest.raises(TypeError, match="models must be a list"):
        model_selector(models)



# test invalid model typeerror

def test_ivalid_model_type():
    models = [ ["version", "v1", "auc", 0.81]]
    
    with pytest.raises(TypeError, match = "model must be a dictionary"):
         model_selector(models)
    
# mepty model

def test_empty_model_situation():
    
    models = [ {}, {}, {} ]
    
    assert model_selector(models)== {}
        