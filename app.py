from flask import Flask, jsonify

app = Flask(__name__)

avances = [
    {
        "fecha": "2024-05-01",
        "descripcion": "Se colocaron los cimientos.",
        "imagen_url": "https://ejemplo.com/imagenes/cimientos.jpg"
    },
    {
        "fecha": "2024-05-03",
        "descripcion": "Inicio de levantamiento de muros.",
        "imagen_url": "https://ejemplo.com/imagenes/muros.jpg"
    }
]

@app.route('/avances', methods=['GET'])
def obtener_avances():
    return jsonify(avances)

if __name__ == '__main__':
    app.run(debug=True)
