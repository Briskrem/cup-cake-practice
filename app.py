"""Flask app for Cupcakes"""
from flask import Flask, render_template, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from form import AddCupcake

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)



@app.route('/')
def index():
    form = AddCupcake()
    return render_template('index.html', form=form)


@app.route('/api/cupcakes')
def list_cupcakes():
    cupcake_list = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcake_list)


@app.route('/api/cupcakes/<int:cake_id>')
def get_cupcake(cake_id):
    cupcake = Cupcake.query.get(cake_id).serialize()
    return jsonify(cupcake = cupcake)


@app.route('/api/cupcakes', methods=['POST'])
def adding_cupcakes():   
    data = request.json
    print('**********************************************')
    print(data)
    cupcake = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=data['image'] or None)
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:cake_id>', methods=['PATCH'])
def update_cupcakes(cake_id):
    cupcake = Cupcake.query.get_or_404(cake_id)
    
    data = request.json
    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake = cupcake.serialize())


@app.route('/api/cupcakes/<int:cake_id>', methods=['DELETE'])
def delete_cupcake(cake_id):
    cupcake = Cupcake.query.get_or_404(cake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message = "deleted")
