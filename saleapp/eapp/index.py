from operator import index

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    categories = [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 2,
        'name': 'Tablet'
    }, {
        'id': 3,
        'name': 'Laptop'
    },]
    products = [{
        "id": 1,
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        "category_id": 1
    }, {
        "id": 2,
        "name": "iPad Pro 2020",
        "description": "Apple, 128GB, RAM: 6GB",
        "price": 37000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        "category_id": 2
    }, {
        "id": 3,
        "name": "Galaxy Note 14 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1
    }, {
        "id": 4,
        "name": "iPhone 18 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 38000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        "category_id": 1
    }, {
        "id": 5,
        "name": "iPad Pro 2026",
        "description": "Apple, 128GB, RAM: 6GB",
        "price": 30000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        "category_id": 2
    }, {
        "id": 6,
        "name": "Galaxy Note 66 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 66000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1
    }]
    filtered = products
    kw = request.args.get('kw')
    category_id = request.args.get('category_id')
    if category_id:
        category_id = int(category_id)
        filtered = [p for p in products if p['category_id'] == category_id]

    if kw:
        filtered = [p for p in products if kw.lower() in p['name'].lower()]

    return render_template('index.html', categories=categories, products=filtered)


@app.route("/register")
def register():
    return 

if __name__ == "__main__":
    app.run(debug=True)