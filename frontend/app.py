from flask import Flask, request
from dotenv import load_dotenv
import os
import pymongo


app = Flask(__name__)

load_dotenv()
MONGO_URI=os.getenv('MONGO_URI')

client=pymongo.MongoClient(MONGO_URI)
db = client['todo_db']
todos_collection = db['todos']

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form['itemName']
    item_desc = request.form['itemDescription']
    todos_collection.insert_one({
        'itemName': item_name,
        'itemDescription': item_desc
    })
    return "Item successfully added!"
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('todo.html')
