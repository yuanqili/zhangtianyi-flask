from app import app


@app.shell_context_processor
def make_shell_context():
    from app import db
    from app.models import Customer, Category, Supplier, Product
    return {
        'db': db,
        'Customer': Customer,
        'Category': Category,
        'Supplier': Supplier,
        'Product': Product,
    }


if __name__ == '__main__':
    # starts the Flask server, listening to localhost:23333
    app.run(host='0.0.0.0', port=23333, debug=True)
