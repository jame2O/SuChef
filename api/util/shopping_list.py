from grocery import get_all_named_item
import json
import pandas as pd
import numpy as np

def get_quantities():
    
    ## Declare the recipe dataframe and 
    recipe_df = pd.DataFrame({})
    with open("./api/data/test_data.json") as f:
        recipe_df = pd.read_json(f)
    f.close()
    recipe_df = pd.read_json(json.dumps(recipe_df.data[0]))
    total_quants = {}
    
    for i, r in recipe_df.iterrows():
        ingredients = pd.json_normalize(r.ingredients)
        for index, row in ingredients.iterrows():
            row.fillna(0)
            ing_name = row["name"]
            ing_quantity = 0
            ing_unit = ""
            if not pd.isna(row["quantity.quantity"]):
                try: 
                    ing_quantity = int(row["quantity.quantity"])
                except ValueError:
                    ing_quantity = 1    
                
                ing_unit = row["quantity.unit"]
            elif not pd.isna(row["quantity"]) and row["quantity"].isnumeric():
                ing_quantity = int(row["quantity"])
                ing_unit = row["quantity.unit"]
                
            # Add quantities if they're already present in the list
            if ing_name in total_quants:
                if isinstance(ing_quantity, int):
                    total_quants[ing_name]['quantity'] += (ing_quantity)
            else:
                total_quants[ing_name] = {
                        "quantity": ing_quantity,
                        "unit": ing_unit,
                    }
    print(pd.DataFrame(total_quants).T)
    return pd.DataFrame(total_quants).T


if __name__ == '__main__':
    sl = get_quantities()
    with open(f'./api/data/test_shopping_list.csv', 'w') as f:
        sl.to_csv(f, index_label="name", na_rep="N/A", lineterminator='\n')
        f.close()
    with open(f'./api/data/test_shopping_list.json', 'w') as f:
        sl.to_json(f, orient='index', indent=4)
        f.close()
        
        
        
            