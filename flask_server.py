
from flask import Flask, render_template, request, send_from_directory
import open_ai
import unsplash

app = Flask(__name__, static_url_path='')


@app.route('/templates/<path:path>')
def send_templates(path):
    return send_from_directory('templates', path)


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
    unsplash_result = ""
    if request.method == 'POST':
        user_input = request.form.get('user_input')

        api_response = open_ai.openai_request(user_input)

        unsplash_result = unsplash.search_unsplash(user_input, 3)

        id1 = unsplash_result[0]
        id2 = unsplash_result[1]
        id3 = unsplash_result[2]

        api_response=api_response+"background-image:<img src='https://unsplash.com/photos/" + id1 + "'alt='' width='' height=''>" +"<img src='https://unsplash.com/photos/" + id2 + "'>" + "<img src='https://unsplash.com/photos/" + id3 + "'>"
        #with open("output.html", "w", encoding='utf-8') as file:
        #    file.write("background-image:<img src='https://unsplash.com/photos/" + id1 + "'alt='' width='' height=''>" +
        #               "<img src='https://unsplash.com/photos/" + id2 + "'>" + "<img src='https://unsplash.com/photos/" + id3 + "'>")

     # return '''{}'''.format(api_response)

    return render_template('index.html', api_response=api_response, unsplash_results=unsplash_result)
