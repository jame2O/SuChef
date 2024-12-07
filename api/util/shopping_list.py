from grocery import get_all_named_item
import json
import pandas as pd
import numpy as np

def get_quantities():
    
    ## Declare the recipe dataframe and 
    recipe_df = pd.DataFrame({})
    with open("./MealPrep/api/data/test_data_2.json") as f:
        recipe_df = pd.read_json(f)
    f.close()
    print (recipe_df)
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

def process_groceries(data: pd.DataFrame, stores):
    for i, r in data.iterrows():
        print(r)
        items_table = get_all_named_item(i, stores)
        # Sort by unitprice and drop dupes
        items_table = items_table.drop_duplicates()
        items_table = items_table.sort_values(by='UnitPrice')
        print(items_table)
        for gi, gr in items_table.iterrows():
            # We first check the units match
            if compare_units(r["unit"], gr["UnitType"]):
                # Units match, get numeric value from quantity
                gr_quant = quant_to_int(gr["Quantity"])
                # Now quantity checks
                sl_quant = r["quantity"]
                needed_quant = 0
                remainder_quant = 0
                if sl_quant > gr_quant:
                    # Case that the needed quant is > than grocery quant
                    
                    needed_quant = sl_quant // gr_quant
                    remainder_quant = sl_quant % gr_quant 
                elif gr_quant < gr_quant:
                    # Case that the needed quant is < than grocery quant
                    
                    needed_quant = 1
                    remainder_quant = sl_quant % gr_quant
                else:
                    # Case that the needed quant == grocery quant
                    
                    needed_quant = 1
                    remainder_quant = 0
                    
                
            else:
                # Units don't match, so perform unit conversions
                sl_quant = convert_units_to_metric(r["unit"], gr["UnitType"])
                gr_quant = quant_to_int(gr["Quantity"])
                
                
                
def quant_to_int(text):
    res = []
    x=list(text)
    for i in x:
        if i.isnumeric():
            res.append(int(i))
    
    return int(''.join([str(n) for n in res]))          
     
def compare_units(sl_unit, gr_unit):
    if sl_unit == gr_unit:
        return True

    return False

def convert_units_to_metric(u1, u2):
    # We only need to have tables for liquid and solid metric measurements
    metric_liquid_factors = {
        'ml': 1,
        'l': 1000,
        'tsp': 4.92892,
        'tbsp': 14.7868,
        'fl oz': 29.5735,
        'cup': 240,
        'pint': 473.176,
        'quart': 946.353,
        'gallon': 3785.41,
    }
    metric_solid_factors = {
        'tsp': 4.92892,
        'tbsp': 14.7868,
        'oz': 29.5735,
        'lb': 453.592,
        'g': 1,
        'kg': 1000
    }
    
    if u2 in metric_liquid_factors.keys():
        return metric_liquid_factors[u1]
    
    if u2 in metric_solid_factors.keys():
        return metric_solid_factors[u1]
    
    raise ValueError(f"Unsupported units: {u1} or {u2}")

def lookup_grocery():
    pass
if __name__ == '__main__':
    sl = get_quantities()
    process_groceries(sl, [1,2,3,4])
    
    with open(f'./MealPrep/api/data/test_shopping_list.csv', 'w') as f:
        sl.to_csv(f, index_label="name", na_rep="N/A", lineterminator='\n')
        f.close()
    with open(f'./MealPrep/api/data/test_shopping_list.json', 'w') as f:
        sl.to_json(f, orient='index', indent=4)
        f.close()
        
        
        
            