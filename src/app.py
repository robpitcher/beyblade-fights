from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory storage for beyblade results (replace with a database in production)
results = []

@app.route('/')
def home():
    return "Welcome to the Beyblade Fight Results App!"

@app.route('/results', methods=['GET'])
def get_results():
    """Get all fight results."""
    return jsonify(results), 200

@app.route('/results', methods=['POST'])
def log_result():
    """Log a new fight result."""
    data = request.get_json()

    # Validate input
    if 'fighter1' not in data or 'fighter2' not in data or 'winner' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    # Create a new result entry
    result = {
        'fighter1': data['fighter1'],
        'fighter2': data['fighter2'],
        'winner': data['winner'],
        'timestamp': data.get('timestamp', 'N/A')  # Optional timestamp
    }
    results.append(result)
    return jsonify(result), 201

if __name__ == '__main__':
    app.run()