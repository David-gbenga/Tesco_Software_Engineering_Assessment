"""
Question 4: Online Search
Build a Search Result Ranking Function Question Given a search query and a collection of product titles, return the top k matching products. Ranking rules:

More query term matches rank higher
Shorter title wins ties
Alphabetical order wins remaining ties Input query = "organic milk"
products = [ "Organic Whole Milk", "Organic Semi Skimmed Milk", "Milk Chocolate", "Organic Eggs" ]

k = 2

Output [ "Organic Whole Milk", "Organic Semi Skimmed Milk" ]

Explanation Both contain: organic + milk

2 matches

Rank by title length. Test Focus • Case insensitive search • Empty query • Empty catalog • Tie-breaking • Products with no matches


"""
from typing import List

import re


"""
def tokenise(text:str)->List[str]:
    
    Converts text into lowercase searchable terms.

    Example:
        "Organic Whole Milk" -> ["organic", "whole", "milk"]
    
    return re.findall(r"[a-zA-Z0-9]+",text.lower())  
"""


def rank_products(products :List[str],query:str, k:int)->List[str]:
    
    if not isinstance(products, list):
        raise TypeError("products must be a list")
    
    if not isinstance(query, str):
        raise TypeError("query must a stirng")
    
    if not isinstance(k,int):
        raise TypeError("k must be an integer")
    
    if not products:
        return []
    
    if not query.strip():
        return []
    
    if k < 0:
        return []
    
    ranking_list = []
    
    query_terms = set(query.lower().split(" "))
    
    for product in products:
        product_terms = set(product.lower().split(" "))
        
        match_count = len(query_terms.intersection(product_terms))
        
        if match_count ==0:
            continue
        
        ranking_list.append((-match_count,len(product),product.lower(),product))
        
        
        
    
    ranking_list.sort()
    
    
    return [product for _,_,_,product in ranking_list[:k]]
    
    
   
    
    
    
    
    
    
 
    
    
    
    
    
    












if __name__=="__main__":
    
    query = "organic milk"
    products = [ "Organic Whole Milk", "Organic Semi Skimmed Milk", "Milk Chocolate", "Organic Eggs" ]

    k = 2
    
    result = rank_products(products, query, k)
    
    print(result)