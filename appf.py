import sklearn
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
filename = 'pipeline.sav'
model = joblib.load(filename)

@app.route('/', methods=['GET', 'POST'])  # Allow both GET and POST
def home():
    if request.method == 'POST':  # Only handle POST if method is POST
        text = request.form['text']
        prediction = predict(text)
        return render_template('index.html', result=prediction)
    return render_template('index.html')  # Handle GET request

def predict(text):
    review = [text]  # Format the input text as a list
    prediction = 'FAKE' if model.predict(review) == 0 else 'REAL'
    return prediction

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for easier troubleshooting

