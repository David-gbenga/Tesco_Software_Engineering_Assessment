import pytest

from online_search import rank_products


#test normal case 

def test_ranking_products():
    query = "organic milk"
    products = [ "Organic Whole Milk", "Organic Semi Skimmed Milk", "Milk Chocolate", "Organic Eggs" ]

    k = 2
    
    assert rank_products(products, query, k)==['Organic Whole Milk', 'Organic Semi Skimmed Milk']
    
    
def test_query_missing():
    query = " "
    products = [ "Organic Whole Milk", "Organic Semi Skimmed Milk", "Milk Chocolate", "Organic Eggs" ]

    k = 2
    
    assert rank_products(products, query, k)==[]
    
def test_return_matching_products():
    query = "eggs"
    products = [ "Organic Whole Milk", "Organic Semi Skimmed Milk", "Milk Chocolate", "Organic Eggs" ]

    k = 2
    
    assert rank_products(products, query, k)==["Organic Eggs"]    
        