from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

# Página de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        # Lógica de registro aquí (almacenamiento en base de datos, etc.)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/api/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = [
        {"name": "Margherita", "ingredients": ["Tomate", "Mozzarella", "Albahaca"], "price": 8.99, "image_url": url_for('static', filename='images/margherita.jpg')},
        {"name": "Pepperoni", "ingredients": ["Pepperoni", "Mozzarella", "Salsa de tomate"], "price": 10.99, "image_url": url_for('static', filename='images/pepperoni.jpg')},
        {"name": "Cuatro Quesos", "ingredients": ["Mozzarella", "Parmesano", "Gorgonzola", "Queso de cabra"], "price": 12.49, "image_url": url_for('static', filename='images/cuatro_quesos.jpg')},
        {"name": "Hawaiana", "ingredients": ["Piña", "Jamón", "Mozzarella"], "price": 11.49, "image_url": url_for('static', filename='images/hawaiana.jpg')},
        {"name": "Barbacoa", "ingredients": ["Carne de res", "Cebolla", "Salsa barbacoa", "Mozzarella"], "price": 13.99, "image_url": url_for('static', filename='images/barbacoa.jpg')},
        {"name": "Vegetariana", "ingredients": ["Pimientos", "Cebolla", "Tomate", "Aceitunas", "Mozzarella"], "price": 9.99, "image_url": url_for('static', filename='images/vegetariana.jpg')},
        {"name": "Carbonara", "ingredients": ["Panceta", "Huevo", "Parmesano", "Mozzarella"], "price": 12.99, "image_url": url_for('static', filename='images/carbonara.jpg')},
        {"name": "Mexicana", "ingredients": ["Chorizo", "Jalapeños", "Cebolla", "Mozzarella"], "price": 13.49, "image_url": url_for('static', filename='images/mexicana.jpg')},
        {"name": "Prosciutto", "ingredients": ["Jamón", "Tomate", "Mozzarella", "Orégano"], "price": 10.49, "image_url": url_for('static', filename='images/prosciutto.jpg')},
        {"name": "Napolitana", "ingredients": ["Anchoas", "Aceitunas", "Ajo", "Tomate", "Mozzarella"], "price": 12.99, "image_url": url_for('static', filename='images/napolitana.jpg')}
    ]
    return jsonify(pizzas)


# Ruta para cargar la página del menú
@app.route('/menu')
@app.route('/')
def menu():
    return render_template('menu.html')


if __name__ == '__main__':
    app.run(debug=True)
