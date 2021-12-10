from flask import Flask, jsonify, request
from flask.templating import render_template
app = Flask(__name__)
from tempDB import products
from tempDB import orders
from tempDB import cart_items
from tempDB import users_info

"""
    getProducts -- GET

    getProductById -- GET (id as parameter from url)

    getOrdersForUser -- GET

    getCartItemsForUser -- GET id as parameter from url)

    createNewProduct -- POST

    addItemToCart -- POST (user_id and product_id as parameter)

    removeItemFromCart -- POST (user_id and product_id as parameter)

    incrementCartItemQuantityByOne -- POST (user_id,cart_item_id)

    decrementCartItemQuantityByOne -- POST (user_id,cart_item_id)

"""

@app.route('/getProducts',methods=['GET'])
def getProducts():
    return jsonify(products)

@app.route('/getProductById',methods=['GET'])
def getProductById():
    id = request.args.get("id")
    return jsonify(products[int(id)-1])

@app.route('/getOrdersForUser',methods=['GET'])
def getOrdersForUser():
    user_id = request.args.get("id")
    return jsonify(orders)

@app.route('/getCartItemsForUser',methods=['GET'])
def getCartItemsForUser():
    user_id = request.args.get("id")
    return jsonify(cart_items)

@app.route('/getUserInfo',methods=['GET'])
def getUserInfo():
    user_id = request.args.get("id")
    return jsonify(users_info[int(user_id)-1])


if __name__ =='__main__':
    app.run(debug=True,port=5001)