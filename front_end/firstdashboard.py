from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/')
def index():
    return render_template('Test_Page.html') #this has changed

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