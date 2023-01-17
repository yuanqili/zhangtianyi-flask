from flask import render_template, request

from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    name = request.args.get('name', 'Stranger')
    gender = request.args.get('gender', 'neutral')
    title = {'male': 'Mr.', 'female': 'Ms.', 'neutral': 'Mx.'}[gender.lower()]
    tweets = [
        {
            'user': 'james',
            'text': 'I love the weather today.',
            'date': 'Jan 11th, 2023',
        },
        {
            'user': 'donald trump',
            'text': 'Make America Great Again!',
            'date': 'Jan 10th, 2023',
        },
        {
            'user': 'Clinton',
            'text': 'I did not have sexual relations with my intern.',
            'date': 'Jan 11th, 2023',
        }
    ]
    return render_template('index.html', name=name, gender=gender, tweets=tweets)


@app.route('/secret')
def secret():
    return 'Ha you found the secret!'
