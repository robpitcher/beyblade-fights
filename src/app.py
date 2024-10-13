from flask import Flask, jsonify, request, render_template

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

    result = {
        'fighter1': data['fighter1'],
        'fighter2': data['fighter2'],
        'winner': data['winner'],
        'timestamp': data.get('timestamp', 'N/A')
    }
    results.append(result)
    return jsonify(result), 201

if __name__ == '__main__':
    app.run(debug=True)
