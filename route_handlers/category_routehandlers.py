import json

from flask import jsonify, request

from repostories.category_repository import CategoryRepository

repository = CategoryRepository()
def get_categories():
    data = repository.fetch_all_categories()
    return jsonify(data)

def get_category_by_id(category_id):
    category = repository.fetch_category_by_id(category_id)
    return jsonify(category) if category else ('category not found')


def create_category():
    new_category = request.json
    data = repository.add_category(new_category["category_name"],new_category["description"])
    print(type(data))
    return jsonify(data)

def update_category(category_id):
    updated_category = request.json
    data = repository.update_category_data(category_id,updated_category["category_name"],updated_category["description"]) 
    return jsonify(data)

def delete_category(category_id):
    data = repository.delete_category_data(category_id)
    return jsonify(data)