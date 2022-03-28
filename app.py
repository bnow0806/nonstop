from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.uccn3.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('page_one.html')     #default page 설정

@app.route('/page_one')
def page_one():
    return render_template('page_one.html')

@app.route('/page_two')
def page_two():
    return render_template('page_two.html')

@app.route('/page_three')
def page_three():
    return render_template('page_three.html')

@app.route('/page_four')
def page_four():
    return render_template('page_four.html')

@app.route('/page_five')
def page_five():
    return render_template('page_five.html')



@app.route("/guest", methods=["POST"])
def guest_post():
    guest_receive = request.form['guest_give']

    guest_list = list(db.guest.find({}, {'_id': False}))
    count = len(guest_list)+1

    doc = {'num': count,
           'guest': guest_receive,
           'done':0
           }
    db.guest.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})

@app.route("/guest", methods=["GET"])
def guest_get():
    guest_list = list(db.guest.find({}, {'_id': False}))

    return jsonify({'guests': guest_list})

@app.route("/preview", methods=["GET"])
def preview_get():
    preview_list = list(db.preview.find({}, {'_id': False}))

    return jsonify({'previews': preview_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)