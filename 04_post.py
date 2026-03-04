from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/usuarios", methods=["POST"])
def crear_usuario():
    data = request.get_json()
    return jsonify({"mensaje": "Usuario creado"}), 201

if __name__ == "__main__":
    app.run(debug=True)