from flask import Flask, render_template, request
from jinja2 import Template

import json

app = Flask(__name__)
app.static_folder = 'static'

def get_clips():
    with open("data/clips.json", 'r') as json_file:
        data = json.load(json_file)
    return data


def format_time(time_string):

    # take time_string and format
    time_string = time_string.replace('T',' ')
    time_string = time_string[:-1]

    return time_string

def is_clip_in_search(clip, word):
    return word.lower() in clip['title'].lower()
    
@app.route('/', methods=['GET'])
def index():

    data = get_clips()
    print(request.args)
    if "search" in request.args:
        word = request.args["search"]
        search_data = []
        for clip in data:
            if is_clip_in_search(clip, word):
                search_data.append(clip)
        data = search_data


    # generate data[i]['sentiment_color']
    for clip in data:
        if clip["score"] < 0:
            clip["sentiment_color"]="red"
        else: 
            clip["sentiment_color"]= "green"

    return render_template('Test_Page.html', data = data, format_time=format_time) #this has changed
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