from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
import ollama
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama2"  # Change if using another model (mistral)

@app.route('/')
def home():
    return render_template('login.html')

# Hardcoded user credentials for demonstration
USERNAME = 'user1'
PASSWORD = 'abc'

@app.route('/', methods=['GET', 'POST'])
def login():

    #print("come in") #This line is for debugging.

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == USERNAME and password == PASSWORD:
            today = datetime.today().strftime('%d/%m/%Y')  # Format date as 31/02/2025
            return render_template("index.html", today_date=today)
        else:
            return render_template("error.html")

    return render_template('index.html')

@app.route('/error')
def error_page():
    return render_template('error.html')

@app.route('/Finance.html')
def finance_page():
    return render_template('Finance.html')


@app.route('/topic.html')
def topic_page():
    return render_template('topic.html')

@app.route('/accountopening.html')
def accountopening_page():
    return render_template('accountopening.html')

@app.route('/insurance.html')
def insurance_page():
    return render_template('insurance.html')


@app.route('/Survivalskills.html')
def Survivalskills_page():
    return render_template('Survivalskills.html')

@app.route('/fire.html')
def fire_page():
    return render_template('fire.html')

@app.route('/cooking.html')
def cooking_page():
    return render_template('cooking.html')

@app.route('/cuisine.html')
def cuisine_page():
    return render_template('cuisine.html')

@app.route('/recipe.html')
def recipe_page():
    return render_template('recipe.html')


@app.route('/chocolate.html')
def chocolate_page():
    return render_template('chocolate.html')

@app.route('/mochi.html')
def mochi_page():
    return render_template('mochi.html')

@app.route('/shortcake.html')
def shortcake_page():
    return render_template('shortcake.html')

@app.route('/pudding.html')
def pudding_page():
    return render_template('pudding.html')

@app.route('/salted-cookies.html')
def salted_page():
    return render_template('salted-cookies.html')

@app.route('/music.html')
def music_page():
    return render_template('music.html')

@app.route('/bakinggame.html')
def Bakinggame_page():
    return render_template('bakinggame.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")

    response = ollama.generate(model=MODEL_NAME, prompt=user_input)
    print(response)
    print(response['response'])
    return jsonify({"response": response['response']})
    
    return jsonify({"response": bot_response})
    #return jsonify({"response": "HIW"})

if __name__ == '__main__':
    app.run(debug=True)


# with open("templates/index.html", "w") as f:
#     f.write(html_content)
