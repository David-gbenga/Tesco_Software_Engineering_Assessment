"""
1. Build a product recommendation function
Question:
Given a customer’s purchase history and a product co-purchase table, return the top k recommended products not already purchased.
Input:
purchase_history = ["milk", "bread"]
co_purchases = { "milk": {"cereal": 5, "bread": 3, "eggs": 2}, "bread": {"butter": 4, "milk": 3} }
k = 2
Output: ["cereal", "butter"]
Test focus: excludes already purchased items, sorts by score, handles empty history.



"""
from typing import List, Dict, Tuple, Mapping
from collections import defaultdict

product = str
score = int
co_purchase = Mapping[product , Mapping[product,score]]


def recommendation_product(purchase_history:List[product],co_purchase,k:int)->List[product]:
    
    #validate the input
    if k <=0:
        return []
    
    if not purchase_history:
        return []
    
    if not co_purchase:
        return []
    
    #create a empty or dictionary with defaultdict to store empty products
    recommend = defaultdict(int)
    
    # remove duplicate products
    purchased = set(purchase_history)
    
    #loop through the purchased goods amd segregate the non purchased goods
    for product in purchased:
        items = co_purchase.get(product,{})
        for prod, score in items.items():
            if prod not in purchased:
                recommend[prod]+=score
                
    # sort products using the score from highest to lowest and the alpgabetical names of the products            
                
    final_product_list = sorted(recommend.keys(), key = lambda prod: (-recommend[prod], prod))
    # return the list top kth products
    
    
     
    return final_product_list[:k]       
                
   
   
   
if __name__=="__main__":
    ph = ["milk", "bread"]
    co = { "milk": {"cereal": 5, "bread": 3, "eggs": 2}, "bread": {"butter": 4, "milk": 3} }
    k = 2
       
    result =recommendation_product(ph,co,k)   
       
    print(result)      
    

    
    
    
    
    
    
    
    
    
    
    
    """
    
    1. Why was a class created or not?

In this solution, I did not create a class because the task is mainly a stateless recommendation calculation.

2. What algorithm/data structure was used?

I used a hashmap-based aggregation algorithm.

The key data structures are:

set(purchase_history)

This gives fast lookup to check whether a product has already been purchased.

defaultdict(int)

This is used as a hashmap to accumulate recommendation scores.

3. Time complexity

Let:

p = number of purchased products
c = total number of co-purchased candidate products checked
r = number of unique recommended products

Creating the purchased set:

O(p)

Looping through co-purchases:

O(c)

Sorting recommendations:

O(r log r)

So the total time complexity is:

O(p + c + r log r)

The sorting step is usually the most expensive part.

4. Space complexity

The purchased set stores the customer’s purchased products:

O(p)

The recommendation dictionary stores candidate products:

O(r)

So total space complexity is:

O(p + r)

Strong Interview Answer

I would say:

I did not create a class because this implementation is a stateless utility-style function. It takes purchase history, co-purchase data, and k, then returns recommendations without needing to preserve internal state. For this coding task, a function keeps the solution simple and readable.

The main algorithm is hashmap-based score aggregation. I use a set for purchased products to achieve constant-time lookup when excluding already purchased items, and I use a dictionary/defaultdict to accumulate recommendation scores. After aggregation, I sort candidates by descending score and alphabetically for deterministic tie-breaking.

The time complexity is O(p + c + r log r), where p is the number of purchased products, c is the number of co-purchase relationships scanned, and r is the number of unique recommendation candidates. The sorting step dominates when many recommendations exist.

The space complexity is O(p + r) because I store the purchased products in a set and the recommendation candidates in a dictionary.

In production, I could improve this with OOP by creating a ProductRecommender class, applying encapsulation, separating validation from recommendation logic, and using strategy patterns so we can support co-purchase recommendations, ML-based recommendations, seasonal recommendations, or personalised ranking without changing the core interface.

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """