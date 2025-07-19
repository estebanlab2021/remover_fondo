#import io
from flask import Flask, request
from flask_cors import CORS  # Importa la extensión CORS
from rembg import remove

app = Flask(__name__)

CORS(app, origins="https://estebanlab2021.github.io")  # Habilita CORS en toda la aplicación

@app.route('/remover-fondo', methods=['POST'])
def remover_fondo():
    if 'image' not in request.files:
        return "No se ha subido una imagen", 400

    image_file = request.files['image']
    input_image = image_file.read()

    # Procesa la imagen usando la librería rembg
    output_image = remove(input_image)

    if not output_image:
        return "La imagen no pudo ser procesada por el servidor.", 500
    
    # Retorna los datos binarios directamente, sin usar send_file
    return output_image, 200, {'Content-Type': 'image/png'}

if __name__ == '__main__':
    app.run(debug=True)
