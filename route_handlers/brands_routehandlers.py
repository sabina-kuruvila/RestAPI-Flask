import json

from flask import jsonify, request

from repostories.brand_repository import BrandRepository

repository = BrandRepository()

def get_brands():
    data = repository.fetch_all_brands()
    return jsonify(data)

def get_brand_by_id(brand_id):
    brand = repository.fetch_brand_by_id(brand_id)
    return jsonify(brand) if brand else ('brand not found')


def create_brand():
    new_brand = request.json
    data = repository.add_brand(new_brand["brand_name"],new_brand["description"])
    print(type(data))
    return jsonify(data)

def update_brand(brand_id):
    updated_brand = request.json
    data = repository.update_brand_data(brand_id,updated_brand["brand_name"],updated_brand["description"]) 
    return jsonify(data)

def delete_brand(brand_id):
    data = repository.delete_brand_data(brand_id)
    return jsonify(data)