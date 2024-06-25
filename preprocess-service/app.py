import os
import logging
from flask import Flask, request, jsonify

LOG_FOLDER = 'logs'

app = Flask(__name__)
app.secret_key = 'supersecretkey'

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

@app.route('/preprocess', methods = ['POST'])
def preprocess():
    logging.info('This is a placeholder function, preprocessing functions yet to be integrated.')
    return 'File successfully preprocessed'

if __name__ == '__main__':
    logging.info('Starting Flask application')
    app.run(debug=True, host='0.0.0.0', port=5002)