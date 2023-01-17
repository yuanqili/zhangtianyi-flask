from app import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(256), index=True)
    contact_name = db.Column(db.String(256), index=True)
    address = db.Column(db.String(256))
    city = db.Column(db.String(256))
    postal_code = db.Column(db.String(256))
    country = db.Column(db.String(256))

    def __repr__(self):
        return f'<Customer [{self.id}] {self.customer_name}>'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(256), index=True)
    description = db.Column(db.String(256))

    def __repr__(self):
        return f'<Category [{self.id}] {self.category_name}>'


class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(256), index=True)
    contact_name = db.Column(db.String(256))
    address = db.Column(db.String(256))
    city = db.Column(db.String(256))
    postal_code = db.Column(db.String(256))
    country = db.Column(db.String(256))
    phone = db.Column(db.String(256), index=True)

    def __repr__(self):
        return f'<Supplier [{self.id}] {self.supplier_name}>'


class Product(db.Model):
    # columns
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(256), index=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    unit = db.Column(db.String(256))
    price = db.Column(db.Float)

    # relationship
    supplier = db.relationship('Supplier', backref=db.backref('products', lazy='dynamic'))
    category = db.relationship('Category', backref=db.backref('products', lazy='dynamic'))

    def __repr__(self):
        return f'<Product [{self.id}] {self.product_name}>'
