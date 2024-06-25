import os
import logging
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
LOG_FOLDER = 'logs'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Ensure log directory exists
os.makedirs(LOG_FOLDER, exist_ok=True)

# Configure logging
log_file_path = os.path.join(LOG_FOLDER, 'app.log')
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

@app.route('/', methods=['GET'])
def home():
    logging.info('Home route accessed')
    return "Welcome user!"

@app.route('/uploadfile', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        logging.warning('No file part in request')
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        logging.warning('No selected file in request')
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        logging.info(f'File successfully uploaded to {file_path}')
        return jsonify({'message': 'File successfully uploaded'}), 200
    else:
        logging.warning('Invalid file type')
        return jsonify({'error': 'Allowed file types are pdf'}), 400

@app.route('/preprocess', methods = ['POST'])
def preprocess():
    logging.info('This is a placeholder function, preprocessing functions yet to be integrated.')
    return 'File successfully preprocessed'

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    logging.info('Starting Flask application')
    app.run(debug=True)
