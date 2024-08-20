import json

from flask import jsonify, request

from repostories.product_repository import ProductRepository

#from repostories.product_repository import add_product, delete_product_data, fetch_all_products, fetch_product_by_id, update_product_data

repository = ProductRepository()
def get_products():
    data = repository.fetch_all_products()
    return jsonify(data)

def get_product_by_id(product_id):
    product = repository.fetch_product_by_id(product_id)
    return jsonify(product) if product else ('product not found')


def create_product():
    new_product = request.json
    data = repository.add_product(new_product["product_name"],new_product["price"])
    print(type(data))
    return jsonify(data)

def update_product(product_id):
    updated_product = request.json
    data = repository.update_product_data(product_id,updated_product["product_name"],updated_product["price"]) 
    return jsonify(data)

def delete_product(product_id):
    data = repository.delete_product_data(product_id)
    return jsonify(data)