from flask import Flask, render_template, request, redirect, url_for, session, json, jsonify
import json


app = Flask(__name__)

# read file
with open('data_source.json', 'r') as myfile:
    data = myfile.read()


@app.route("/display_json")
def display_json_in_table():
    data = json.load(open("data_source.json"))
    #return render_template('display_json.html', title="DISPLAY JSON DATA IN HTML", jsondata=json.dumps(data))
    #for user in data["signup_details"]:
    return render_template('display_json.html', title="DISPLAY JSON DATA IN HTML", jsondata=data["signup_details"])





if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)
