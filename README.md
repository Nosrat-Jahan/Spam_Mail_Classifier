# Spam Mail Classifier
**Developer:** Nosrat Jahan  
**Academic Status:** BSc in Computer Science and Engineering

## About the Project
This project is an automated email classification tool designed to identify malicious or unwanted emails. It leverages Machine Learning, specifically the **Multinomial Naive Bayes** algorithm, to analyze text patterns and determine if an email is 'Spam' or 'Ham' (Legitimate).

## Features
- **Real-time Text Analysis:** Instantly classifies user-provided email content.
- **Modern UI:** Built with a clean and responsive interface using Tailwind CSS.
- **Efficiency:** Uses a lightweight model ensuring fast processing and low resource consumption.

## Technologies Used
- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn (TfidfVectorizer, MultinomialNB)
- **Frontend:** HTML5, Tailwind CSS, Google Fonts

## Project Structure
- `app.py`: The main Flask server handles model inference and routing.
- `templates/`: Contains the HTML interface.
- `requirements.txt`: Lists the necessary Python libraries for the environment.

## Installation and Setup
1. Clone the repository to your local machine.
2. Install the required libraries:
   ```bash
   pip install flask scikit-learn
