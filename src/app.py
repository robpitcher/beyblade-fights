from flask import Flask, jsonify, request, render_template
from datetime import datetime, timezone

app = Flask(__name__)

# Sample in-memory storage for beyblade results
results = []

@app.route('/')
def home():
    return render_template('index.html')  # Render the index.html template

@app.route('/results', methods=['GET'])
def get_results():
    return jsonify(results), 200

@app.route('/results', methods=['POST'])
def log_result():
    data = request.get_json()
    if 'fighter1' not in data or 'fighter2' not in data or 'winner' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    now = datetime.now(timezone.utc)
    timestamp_iso = now.isoformat()  # ISO 8601 format
    date_str = now.strftime('%Y-%m-%d')  # Extract date
    time_str = now.strftime('%H:%M:%S')  # Extract time

    result = {
        'fighter1': data['fighter1'],
        'fighter2': data['fighter2'],
        'winner': data['winner'],
        'date': date_str,  # Add date
        'time': time_str,  # Add time
        'timestamp': timestamp_iso
    }
    results.append(result)
    return jsonify(result), 201

@app.route('/results-page')
def results_page():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)