from grocery import get_all_named_item
import json
import pandas as pd
import numpy as np

def get_quantities():
    
    ## Declare the recipe dataframe and 
    recipe_df = pd.DataFrame({})
    with open("./MealPrep/api/data/recipe_data.json") as f:
        recipe_df = pd.read_json(f)
    f.close()
    recipe_df = pd.read_json(json.dumps(recipe_df.data[0]))

    total_quants = {}
    
    for i, r in recipe_df.iterrows():
        ingredients = pd.json_normalize(r.ingredients)
        print(ingredients)
        
    
    for index, row in ingredients.iterrows():
        ing_name = row["name"]
        print(row["quantity.quantity"])
        ing_quantity = 0
        ing_unit = ""
        if not pd.isna(row["quantity.quantity"]):
            ing_quantity = int(row["quantity.quantity"])
            ing_unit = row["quantity.unit"]
        else:
            ing_quantity = row["quantity"]
        if ing_name in total_quants:
            total_quants[ing_name].quantity += ing_quantity
        else:
            total_quants[ing_name] = {
                    "quantity": row["quantity.quantity"],
                    "unit": row["quantity.unit"]
                }
    return total_quants
if __name__ == '__main__':
    print(get_quantities())
        