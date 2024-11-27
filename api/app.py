from flask import Flask, jsonify, request
from flask_cors import CORS
from MealPrep.api.util.grocery import scrape_items
from util.scrape_recipes import scrape_bbc_links, scrape_bbc_recipes
import json
app = Flask(__name__)
CORS(app)
@app.route('/get_recipes', methods=['POST'])
def get_recipes():
    with open('./data/recipes.json', 'r') as d_file:
        recipes_json = json.load(d_file)
        recipes_str = json.dumps(recipes_json)
    return recipes_str
    
if __name__ == '__main__':
    app.run(debug=True)