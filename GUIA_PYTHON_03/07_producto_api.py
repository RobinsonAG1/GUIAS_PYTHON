from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os


load_dotenv()

APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("APP_PORT", 5000))
DEBUG = os.getenv("DEBUG", "False") == "True"


app = Flask(__name__)
CORS(app)

productos_db = []
contador_id = 1


class Producto:

    def __init__(self, nombre, precio, stock):
        global contador_id
        self.__id = contador_id
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        contador_id += 1

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

  
    def actualizar_stock(self, cantidad):
        self.__stock += cantidad

    def aplicar_descuento(self, porcentaje):
        self.__precio -= self.__precio * (porcentaje / 100)

    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "precio": self.__precio,
            "stock": self.__stock
        }


@app.route("/productos", methods=["GET"])
def listar_productos():
    return jsonify([p.to_dict() for p in productos_db]), 200

@app.route("/productos", methods=["POST"])
def crear_producto():
    data = request.get_json()

    nombre = data.get("nombre")
    precio = data.get("precio")
    stock = data.get("stock")

    if not nombre or precio is None or stock is None:
        return jsonify({"error": "Datos incompletos"}), 400

    nuevo_producto = Producto(nombre, precio, stock)
    productos_db.append(nuevo_producto)

    return jsonify(nuevo_producto.to_dict()), 201

if __name__ == "__main__":
    app.run(host=APP_HOST, port=APP_PORT, debug=DEBUG)