
from flask import Flask, render_template, request, send_from_directory
import open_ai
import unsplash

app = Flask(__name__, static_url_path='')


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/favicon/<path:path>')
def send_favicon(path):
    return send_from_directory('favicon', path)

@app.route('/unsplashy/<path:path>')
def send_unsplashy(path):
    return send_from_directory('unsplashy', path)

@app.route('/', methods=['GET', 'POST'])
def root():
    api_response = ""
    if request.method == 'POST':
        user_input = request.form.get('user_input')

        api_response = open_ai.openai_request(user_input)

         #return '''{}'''.format(api_response)

    return render_template('index.html', api_response=api_response)
