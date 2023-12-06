from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definição do modelo de Hotel
class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    cidade = db.Column(db.String(255))
    quartos = db.relationship('Quarto', backref='hotel', lazy=True)

# Definição do modelo de Quarto
class Quarto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(255))
    capacidade = db.Column(db.Integer)
    quarto = db.Column(db.String(255))
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))

# Definição do modelo de Reserva
class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cidade = db.Column(db.String(255))
    hotel = db.Column(db.String(255))
    quarto = db.Column(db.String(255))
    data = db.Column(db.String(255))

# Schema para validação e serialização de Hotel
class HotelSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    cidade = fields.Str(required=True)

# Schema para validação e serialização de Quarto
class QuartoSchema(Schema):
    id = fields.Int(dump_only=True)
    tipo = fields.Str(required=True)
    capacidade = fields.Int(required=True)

# Schema para validação e serialização de Reserva
class ReservaSchema(Schema):
    id = fields.Int(dump_only=True)
    cidade = fields.Str(required=True)
    hotel = fields.Str(required=True)
    quarto = fields.Str(required=True)
    data = fields.Str(required=True)

# Rotas

@app.route('/hoteis/<cidade>', methods=['GET'])
def get_hoteis(cidade):
    hoteis = Hotel.query.filter_by(cidade=cidade).all()
    hotel_schema = HotelSchema(many=True)
    result = hotel_schema.dump(hoteis)
    return jsonify(result)

@app.route('/reservas', methods=['POST'])
def create_reserva():
    reserva_schema = ReservaSchema()
    try:
        data = reserva_schema.load(request.json)
        nova_reserva = Reserva(**data)
        db.session.add(nova_reserva)
        db.session.commit()
        return jsonify(reserva_schema.dump(nova_reserva)), 201
    except ValidationError as err:
        return jsonify({"message": err.messages}), 400

@app.route('/reservas/<int:id>', methods=['PATCH'])
def update_reserva(id):
    reserva = Reserva.query.get(id)
    if reserva is None:
        return jsonify({"message": "Reserva não encontrada"}), 404

    reserva_schema = ReservaSchema()
    try:
        data = reserva_schema.load(request.json, partial=True)
        for key, value in data.items():
            setattr(reserva, key, value)
        db.session.commit()
        return reserva_schema.dumps(reserva)
    except ValidationError as err:
        return jsonify({"message": err.messages}), 400

@app.route('/reservas/<int:id>', methods=['DELETE'])
def delete_reserva(id):
    reserva = Reserva.query.get(id)
    if reserva is None:
        return jsonify({"message": "Reserva não encontrada"}), 404

    db.session.delete(reserva)
    db.session.commit()
    return jsonify({"message": "Reserva excluída com sucesso"})

@app.route('/reservas', methods=['GET'])
def get_reservas():
    reservas = Reserva.query.all()
    reserva_schema = ReservaSchema(many=True)
    result = reserva_schema.dump(reservas)
    return jsonify(result)

@app.route('/reservas/<int:id>', methods=['GET'])
def get_reserva(id):
    reserva = Reserva.query.get(id)
    if reserva is None:
        return jsonify({"message": "Reserva não encontrada"}), 404

    reserva_schema = ReservaSchema()
    return reserva_schema.dump(reserva)


if __name__ == '__main__':
    app.run(debug=True)
