from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

class LoadModel:
    def __init__(self, name, provider):
        self.model = name
        self.provider = provider

    def ask(self, question):
        response = model.generate_content(question)
        # Assuming response has a 'content' attribute or method that contains the generated text
        return {
            "question": question,
            "answer": response.content if hasattr(response, 'content') else str(response)
        }

app = Flask(__name__)
model_loader = LoadModel(name='gemini-1.5-flash', provider='Google')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def ask():
    if request.method == 'POST':
        question = request.form['question']
        answer = model_loader.ask(question=question)
        return jsonify(answer)
    else:
        return 'Wrong Method!', 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
