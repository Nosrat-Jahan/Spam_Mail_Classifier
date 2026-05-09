# Project: Spam Mail Classifier
# Developer: Nosrat Jahan

from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Sample training data
emails = [
    "win money now",
    "Congratulations you won a lottery",
    "Claim your free prize",
    "Earn dollars fast",
    "Meeting scheduled tomorrow",
    "Project discussion at 3pm",
    "Lunch with team today",
    "Please review the report"
]

labels = [
    "spam",
    "spam",
    "spam",
    "spam",
    "ham",
    "ham",
    "ham",
    "ham",
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(X, labels)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    message = request.form["message"]

    data = vectorizer.transform([message])
    prediction = model.predict(data)[0]
    return render_template(
        "index.html",
        prediction=prediction,
        message = message
    )

if __name__ == "__main__":
    app.run(debug=True, port=1010)
