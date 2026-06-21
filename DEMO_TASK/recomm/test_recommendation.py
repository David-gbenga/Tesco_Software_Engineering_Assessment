import pytest


from recommendation import recommendation_product


#test normal case / valid inputs
def test_normal_case_zero():
    ph = ["milk", "bread"]
    co = { "milk": {"cereal": 5, "bread": 3, "eggs": 2}, "bread": {"butter": 4, "milk": 3} }
    k = 2
       
    result =recommendation_product(ph,co,k)
    assert result ==["cereal","butter"]


# Test when k is zero 
def test_k_is_zero():
    ph = ["milk", "bread"]
    co = { "milk": {"cereal": 5, "bread": 3, "eggs": 2}, "bread": {"butter": 4, "milk": 3} }
    k = 0
       
    result =recommendation_product(ph,co,k)
    
    assert result ==[]
    
    
    
    
    
# test when co_purchase is not available 
def test_co_prucahse_not():
    ph = ["milk", "bread"]
    co = { }
    k = 2
       
    result =recommendation_product(ph,co,k)
    
    assert result ==[]    
    
    
def test_exclude_co_purchase_products():
    ph = ["milk", "bread"]
    co = { "milk": {"bread": 3}, "bread": { "milk": 3} }
    k = 0
       
    result =recommendation_product(ph,co,k)
    
    assert result ==[]    
       
    