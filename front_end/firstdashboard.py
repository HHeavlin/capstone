from flask import Flask, render_template, request
from jinja2 import Template

import json

app = Flask(__name__)
app.static_folder = 'static'

def get_clips(channel=None, number=None):
    with open("data/clips.json", 'r') as json_file:
        data = json.load(json_file)

    if not number==None:
        return data[:number]

    if not channel==None:
        word = channel
        search_data = []
        for clip in data:
            if word.lower() == clip['broadcaster'].lower():
                search_data.append(clip)
        data = search_data
    return data


def format_time(time_string):

    # take time_string and format
    time_string = time_string.replace('T',' ')
    time_string = time_string[:-1]

    return time_string

def is_clip_in_search(clip, word):
    return (word.lower() in clip['title'].lower() or
      word.lower() in clip['broadcaster'].lower())


@app.route('/')
def index():
    try:
        data = get_clips(number=1)
    except FileNotFoundError as e:
        ## Process Error
        return "No clips" # Add error page

    for clip in data:
        if clip["score"] < 0:
            clip["sentiment_color"]="red"
        else: 
            clip["sentiment_color"]= "green"

    return render_template('index.html', result=data[0], format_time=format_time)
    
def generic_channels(channel):
    try:
        data = get_clips(channel=channel)
    except FileNotFoundError as e:
        ## Process Error
        return "No clips" # Add error page

    if "search" in request.args:
        word = request.args["search"]
        search_data = []
        for clip in data:
            if is_clip_in_search(clip, word):
                search_data.append(clip)
        data = search_data

    # cut off extra data


    # generate data[i]['sentiment_color']
    for clip in data:
        if clip["score"] < 0:
            clip["sentiment_color"]="red"
        else: 
            clip["sentiment_color"]= "green"

    return render_template('channels.html', data = data, format_time=format_time) 

@app.route('/channels/', methods=['GET'])
def default_channels():
    return generic_channels(None)

@app.route('/channels/<channel>', methods=['GET'])
def specific_channels(channel):
    return generic_channels(channel)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % escape(username)

@app.route('/clips/') 
def clips():
    try:
        data = get_clips()
    except FileNotFoundError as e:
        ## Process Error
        return "No clips" # Add error page

    if "search" in request.args:
        word = request.args["search"]
        search_data = []
        for clip in data:
            if is_clip_in_search(clip, word):
                search_data.append(clip)
        data = search_data
    return render_template('clips.html', data = data, format_time=format_time)

@app.route('/subs/')
def subs():
    return render_template('subs.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/emotes/') 
def emotes():
    try:
        data = get_clips()
    except FileNotFoundError as e:
        ## Process Error
        return "No clips" # Add error page


    if "search" in request.args:
        word = request.args["search"]
        search_data = []
        for clip in data:
            if is_clip_in_search(clip, word):
                search_data.append(clip)
        data = search_data

    with open("emotelinks.json", "r") as f:
        emotelinks = json.load(f)
        

    for clip in data:

        bemote = clip["bemote"] # bemote = "moon2CR"
        bemote_link = emotelinks[bemote]
        bemote_score = 0
        clip['bemote'] = bemote_link


        aemote = clip["aemote"]
        aemote_link = emotelinks[aemote]
        aemote_score = 0
        clip['aemote'] = aemote_link

    return render_template('emotes.html', data = data, format_time=format_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)