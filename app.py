from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained model and vectorizer
with open('phishing_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    # Transform the input URL
    url_vector = vectorizer.transform([url])

    # Predict
    prediction = model.predict(url_vector)[0]
    result = 'Phishing' if prediction == 1 else 'Legitimate'

    return jsonify({'url': url, 'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
