import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods = ['POST'])
def convert():
    currency = request.form.get("currency")
    res = requests.get("http://data.fixer.io/api/latest?access_key=ddc036e61dbcc8bfa08bdc0a50a28250")

    # Make sure request is success
    if res.status_code != 200:
        return jsonify({"success": False})


    # Make sure request is success
    data = res.json()

    if currency not in data["rates"]:
         return jsonify({"success": False})

    return jsonify({"success": True, "rate": data["rates"][currency]})