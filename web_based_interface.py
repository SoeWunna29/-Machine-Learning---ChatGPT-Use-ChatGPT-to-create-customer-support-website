from flask import Flask, render_template, request
import openai
import os

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set up Flask app
app = Flask(__name__)

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for chat API
@app.route('/chat', methods=['POST'])
def chat():
    # Get user's message from POST request
    message = request.form['message']

    # Call OpenAI API to generate response
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5
    )

    # Extract text from response and return it
    text = response.choices[0].text.strip()
    return text

if __name__ == '__main__':
    app.run(debug=True)
