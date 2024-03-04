from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import CORS
from google.cloud import vision
import os
import uuid
import openai

# Set your Google Cloud credentials and OpenAI API key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/marcellopisani/Desktop/HTML local/nifty-cabinet-416210-6f0a382755a4.json'
openai.api_key = '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'

app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file sent'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    if file and allowed_file(file.filename):
        ext = file.filename.rsplit('.', 1)[1].lower()
        unique_filename = f"{uuid.uuid4()}.{ext}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)

        # Process the image with Google Cloud Vision
        client = vision.ImageAnnotatorClient()
        with open(filepath, 'rb') as image_file:
            content = image_file.read()
        image = vision.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations
        extracted_text = texts[0].description if texts else ''

        # Query OpenAI GPT-4 using the chat endpoint
        ai_response = openai.ChatCompletion.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "system", "content": "Sei un assistente che classifica le spese dagli scontrini e fatture.Sei l’assistente di un’app di Budgeting di una nota banca svizzera. Il tuo ruolo sarà quello di analizzare ed imparare a leggere alla perfezione tutti gli scontrini che ti verranno posti. Dovrai analizzare attentamente la foto e riconoscere i seguenti dati: Prezzo in € (soldi spesi) Data di acquisto (data in cui è stato stampato lo scontrino)  La “categoria” di appartenenza della spesa Le “categorie” sono le seguenti: Affitto Alimentari Viaggi Investimenti Medicine e cure Benessere personale Spa Ristoranti  dove ogni categoria è separata da una virgola all'interno del {}.  Output esempio: { Prezzo: ""; Categoria: ""; Data: 'data' } Dovrai inoltre essere in grado di fare lo stesso con delle fatture oltre che con degli scontrini, per riuscire a capire in che categoria smistare la spesa che vedi all’interno della fattura cerca sulla foto o il file sottoposto il mittente ricerca su internet informazioni sul mittente definisci e smista nelle varie categorie Output esempio: { Prezzo: ""; Categoria: ""; Data: 'data' } Dovrai rispondere con soltanto il formato che ti ho chiesto, non aggiungere altro alla tua risposta. "},
        {"role": "user", "content": "Analizza questo scontrino e forniscimi solo l'output richiesto: " + extracted_text}
    ]
        )

        # Access the response properly
        ai_text_response = ai_response['choices'][0]['message']['content'] if ai_response['choices'] else 'No response generated'

        return jsonify({'message': 'File uploaded successfully', 'extracted_text': extracted_text, 'ai_response': ai_text_response}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("static/" + path):
        return send_from_directory('static', path)
    else:
        return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)