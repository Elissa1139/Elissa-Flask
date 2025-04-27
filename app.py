from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
import ollama
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama2"  # Change if using another model (mistral)

chat_history = [
    {
        "role": "system",
        "content": 
             "You are an assistant for a specific website. " +
            "You must ONLY answer questions based on the provided website content. " +
            "If the answer is not present in the website content, politely say 'I don't know based on the website information.' " + 
            f"Here is information about the website named 'Growing Up', where you get information about your daily needs such as opening bank accounts from a popular banks like DBS, OCBC, UOB. Get details on insurance, survival skills, baking receipes, cooking videos. Finally you can get to quiz based on the learnings you did on this website to test whether you learnt well."
        
    }
]

@app.route('/')
def home():
    return render_template('login.html')

# Hardcoded user credentials for demonstration
USERNAME = 'user1'
PASSWORD = 'abc'

@app.route('/login.html', methods=['GET', 'POST'])
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

@app.route('/register.html', methods=['GET', 'POST'])
def register():

    #print("come in") #This line is for debugging.

    if request.method == 'POST':
        USERNAME = request.form['username']
        PASSWORD = request.form['password']
        
        
        today = datetime.today().strftime('%d/%m/%Y')  # Format date as 31/02/2025
        return render_template("index.html", today_date=today)
        

    return render_template('register.html')

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

@app.route('/quiztime.html')
def quiztime_page():
    return render_template('quiztime.html')

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
    chat_history.append({"role": "user", "content": user_input})

    response = ollama.chat(
        model='llama2',
        messages=chat_history
    )

    answer = response['message']['content']
    chat_history.append({"role": "assistant", "content": answer})
    print(chat_history)
    return jsonify({"response": answer})


if __name__ == '__main__':
    app.run(debug=True)


# with open("templates/index.html", "w") as f:
#     f.write(html_content)
