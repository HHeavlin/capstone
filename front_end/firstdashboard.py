from flask import Flask, render_template
from jinja2 import Template

import json

app = Flask(__name__)
app.static_folder = 'static'

def get_clips():
    with open("data/clips.json", 'r') as json_file:
        data = json.load(json_file)
    return data
    
@app.route('/')
def index():

    data = get_clips()

    return render_template('Test_Page.html', data = data) #this has changed
    #                                        username1="Yasmine__", username2="Brian"

@app.route('/channels/')
def channels():
    return render_template('channels.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % escape(username)

@app.route('/subs/')
def subs():
    return render_template('subs.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)